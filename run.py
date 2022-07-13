from dataclasses import dataclass
import subprocess
import signal
from typing import List

import openai
from tqdm import tqdm
import fire
from tree_sitter import Language, Parser

import pandas as pd

import time
from pathlib import Path
from math import prod
from statistics import mean
import textwrap
from types import ModuleType
import re

EMOJI_PASS = "\u2705"  
EMOJI_FAIL = "\u274c"
EMOJI_SYNTAX_ERROR = "\U0001F480"
EMOJI_TIMEOUT = "\u231b"

Language.build_library(
  'build/tree_sitter.so',
  [
    'vendor/tree-sitter-python'
  ]
)

from common import Problem

class ExecutionError(Exception):
    pass

class TimeoutError(Exception):
    pass

PY_LANGUAGE = Language('build/tree_sitter.so', 'python')

def node_to_code(code_bytes, node):
    return str(code_bytes[node.start_byte:node.end_byte], 'utf8')

def extract_first_func(code):
    code_bytes = bytes(code, "utf8")
    lang = PY_LANGUAGE
    q1 = "((function_definition) @f)"
    q2 = "([(import_statement) (import_from_statement)] @f)"

    parser = Parser()
    parser.set_language(lang)
    tree = parser.parse(code_bytes)

    query = lang.query(q1)
    captures = query.captures(tree.root_node)
    if captures:
        node = captures[0][0]
        func = node_to_code(code_bytes, node)

        query = lang.query(q2)
        captures = query.captures(tree.root_node)
        imports = []

        for c in captures:
            if c[0].end_byte <= node.start_byte:
                imports.append(node_to_code(code_bytes, c[0]))

        imports = list(set(imports))
        out_code = "\n".join(imports) + "\n" + func
    else:
        out_code = None

    return out_code

def to_comment(text):
    #return "\n".join(["# " + l for l in text.splitlines()] + ["# Use Python"])
    return '"""' + text + '"""'

def save(problem_name, model_name, index, input, outputs, lang):
    input_dir = Path('./inputs') / model_name / lang / problem_name
    input_dir.mkdir(exist_ok=True, parents=True)

    (input_dir / f"{index}.txt").write_text(input)

    output_dir = Path('./outputs') / model_name / lang / problem_name / str(index)
    output_dir.mkdir(exist_ok=True, parents=True)

    for i, o in enumerate(outputs):
        (output_dir / f"{i}.py").write_text(o)

@dataclass
class Codex:
    temperature: float
    top_p: float 
    n: int
    max_tokens: int

    DEFAULT_TEMPERATURE = 0.0

    def run(self, prompt):
        while True:
            try:
                e = openai.Completion.create(engine='code-davinci-002',
                                prompt=prompt, temperature=self.temperature, top_p=self.top_p,
                                n=self.n, max_tokens=self.max_tokens, echo=True)
                return list(set(filter(None, [c.text for c in e.choices if 'text' in c])))
            except openai.error.RateLimitError:
                print("Rate limit reached. Retrying in 10 seconds...")
                time.sleep(10)
            except openai.error.InvalidRequestError:
                return []

@dataclass
class CodeParrot:
    max_tokens: int
    temperature: float
    cuda: bool = True

    DEFAULT_TEMPERATURE = 0.1
    BOS = "<|endoftext|>"
    def __post_init__(self):
        from transformers import AutoModelForCausalLM, AutoTokenizer
       
        model_name = "codeparrot/codeparrot"

        print("loading model")
        model = AutoModelForCausalLM.from_pretrained(model_name)
        print("loading tokenizer")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        print("loading complete")

        if self.cuda:
            model = model.cuda()

        self.model = model
        self.tokenizer = tokenizer

        # from transformers import pipeline
        # self.pipe = pipeline("text-generation", model="codeparrot/codeparrot", device=0)

    def generate(self, input: str, max_to_generate: int, temperature: float):
        import torch
        """
        Do standard left-to-right completion of the prefix `input` by sampling from the model
        """
        input_ids = self.tokenizer(input, return_tensors="pt").input_ids
        if self.cuda:
            input_ids = input_ids.cuda()
        max_length = max_to_generate
        with torch.no_grad():
            output = self.model.generate(input_ids=input_ids, do_sample=True, top_p=0.95, temperature=temperature, max_length=max_length)
        # pass clean_up_tokenization_spaces=False to avoid removing spaces before punctuation, e.g. "from ." -> "from."
        detok_hypo_str = self.tokenizer.decode(output.flatten(), clean_up_tokenization_spaces=False)
        print(detok_hypo_str)
        if detok_hypo_str.startswith(self.BOS):
            detok_hypo_str = detok_hypo_str[len(self.BOS):]
        return detok_hypo_str

    def run(self, prompt):
        # FIXME: hardcoded for n == 1
        return [self.generate(prompt.strip(), max_to_generate=self.max_tokens, temperature=self.temperature)]

        # outputs = self.pipe(prompt)
        # print(outputs)
        # print(outputs[0]['generated_text'])
        # return [outputs[0]['generated_text']]
        

@dataclass
class InCoder:
    temperature: float
    max_tokens: int
    big_model: bool = True
    cuda: bool = True
    verbose: bool = True

    DEFAULT_TEMPERATURE = 0.2

    BOS = "<|endoftext|>"
    def __post_init__(self):
        import torch
        import tokenizers
        from transformers import AutoModelForCausalLM, AutoTokenizer
       
        if self.big_model:
            model_name = "facebook/incoder-6B"

            # the arguments added below will load a half precision version of the model,
            # which requires less RAM than loading the full float32 version.  this 
            # should fit in ~16GB of RAM
            # NOTE: half precision should *not* be used if you plan to fine-tune the
            # model. You'll need full precision and a lot of GPU memory. We have not
            # tested fine-tuning in `transformers` (the model was trained in fairseq)
            if self.cuda:
                kwargs = dict(
                    revision="float16", 
                    torch_dtype=torch.float16,
                    low_cpu_mem_usage=True,
                )
            else:
                kwargs = dict(
                    low_cpu_mem_usage=True,
                )
        else:
            model_name = "facebook/incoder-1B"
            kwargs = {}

        print("loading model")
        model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
        print("loading tokenizer")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        print("loading complete")

        if self.cuda:
            model = model.half().cuda()

        self.model = model
        self.tokenizer = tokenizer

    def generate(self, input: str, max_to_generate: int, temperature: float):
        import torch
        """
        Do standard left-to-right completion of the prefix `input` by sampling from the model
        """
        input_ids = self.tokenizer(input, return_tensors="pt").input_ids
        if self.cuda:
            input_ids = input_ids.cuda()
        max_length = max_to_generate + input_ids.flatten().size(0)
        if max_length > 2048:
            print("warning: max_length {} is greater than the context window {}".format(max_length, 2048))
        with torch.no_grad():
            output = self.model.generate(input_ids=input_ids, do_sample=True, top_p=0.95, temperature=temperature, max_length=max_length)
        # pass clean_up_tokenization_spaces=False to avoid removing spaces before punctuation, e.g. "from ." -> "from."
        detok_hypo_str = self.tokenizer.decode(output.flatten(), clean_up_tokenization_spaces=False)
        if detok_hypo_str.startswith(self.BOS):
            detok_hypo_str = detok_hypo_str[len(self.BOS):]
        return detok_hypo_str

    def run(self, prompt):
        # FIXME: hardcoded for n == 1
        return [self.generate(prompt, max_to_generate=self.max_tokens, temperature=self.temperature)]

class Main:

    _FAKE_INPUT_FUNC = """
      def input(*args):
          return {input}
    """

    _FAKE_INPUT_FUNC_MANY = """
      input_idx = 0
      def input(*args):
          global input_idx
          input = {input}
          current_input = input[input_idx]
          input_idx += 1
          return current_input
    """

    def _patch_python(self, code, input):
        if isinstance(input, list):
            return textwrap.dedent(self._FAKE_INPUT_FUNC_MANY.format(input=input)) + code
        else:
            return textwrap.dedent(self._FAKE_INPUT_FUNC.format(input=input)) + code

    def _load_model(self, model_name, temperature, top_p, n, max_tokens):
        if model_name == 'codex':
            return Codex(temperature=temperature or Codex.DEFAULT_TEMPERATURE, top_p=top_p, n=n, max_tokens=max_tokens)
        elif model_name == 'incoder':
            return InCoder(temperature=temperature or InCoder.DEFAULT_TEMPERATURE, max_tokens=max_tokens)
        elif model_name == 'codeparrot':
            return CodeParrot(temperature=temperature or CodeParrot.DEFAULT_TEMPERATURE, max_tokens=max_tokens)
        else:
            raise ValueError(f"invalid model '{model_name}'")

    def eval(self, problem_name, temperature=None, top_p=1, n=1, max_tokens=512, dry_run=False, lang='', model='codex'):
        problem = Problem(problem_name)
        gen = problem.generate_func

        model_name = model
        model = self._load_model(model_name, temperature=temperature, top_p=top_p, n=n, max_tokens=max_tokens)

        for text, _vars, index in tqdm(list(gen(lang=lang))):
        # for index, vals in enumerate(tqdm(list(itertools.product(*GRID.values())))):
        #     vars = dict(zip(GRID.keys(), vals))
        #     text = render(**vars)
            if not text:
                continue
            # if not problem.has_target:
            #     input = to_comment(text)
            # else:
            #     input = text
            input = text
            print(input)
            print()

            if not dry_run:
                outputs = model.run(prompt=input)
            else:
                outputs = []

            print(len(outputs))
            save(problem_name, model_name, index, input, outputs, lang)

    def _test_imports_str(self, problem):
        imports = []

        def invalid_import():
            raise ValueError("import must be either str or Tuple[str, str] or Tuple[str, List[str]]")

        for imp in problem.test_imports:
            if isinstance(imp, str): 
                imports.append(f"import {imp}")
            elif isinstance(imp, tuple):
                if len(imp) > 2: invalid_import()
                imp1 = imp[1]
                if not isinstance(imp1, list):
                    imp1 = [imp1]
                imports.append(f"from {imp[0]} import {', '.join(imp1)}")
            else:
                invalid_import()
                
        return '\n'.join(imports) + '\n'

    def _strip_cell_tags(self, text):
        return re.sub(r"</?(?:cell|text)/?>", "", text)

    def _run_python(self, problem, f, vars, lang, model):
        if problem.has_target:
            text = f.read_text()

            if model == 'incoder':
                text = self._strip_cell_tags(text)

            code = extract_first_func(text)
            if code is None:
                raise ExecutionError("no function/method found in output")

            code = self._test_imports_str(problem) + code
            try:
                exec_obj = compile(code, str(f), 'exec')
            except (IndentationError, SyntaxError) as e:
                raise ExecutionError(str(e))

            module = ModuleType(str(f).replace('/', '.'))
            exec(exec_obj, module.__dict__)
            target = getattr(module, problem.get_target_name(vars, lang))
            if not 'input' in vars:
                input = []
            else:
                input = vars['input']
                if not isinstance(input, list): input = [input]

            print('input', input)

            try:
                signal.alarm(10)
                return target(*input)
            except (NameError, TypeError, ValueError, IndexError, RecursionError, ZeroDivisionError, AttributeError) as e:
                raise ExecutionError(str(e))
            # mod = __import__(str(f).replace('/', '.'))
            # target = getattr(mod, target)
            # target(*vars['input'])
            # return problem.run_func(target, vars)
        else:
            code = self._patch_python(f.read_text(), vars['input'])
            try:
                output = subprocess.run(['python', '-c', code], check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as e: 
                raise ExecutionError(e.stderr)

            try:
                actual = output.stdout.strip() #.splitlines()[-1]
            except ValueError:
                actual = None

            return actual

    def _sigalarm_handler(self, signum, frame):
        raise TimeoutError("timeout reached")

    def variant_counts(self, lang=''):
        problems: List = [f.stem for f in Path('problems').glob('*.py')]
        problems.remove('default')

        total = 0

        for problem in problems:
            problem = Problem(problem)
            gen = problem.generate_func
            c = len(list(gen(with_inputs=False, lang=lang)))
            total += c
            print(f"{problem}:\t\t\t{c}")
        print(f"Total:\t\t\t{total}")

    def test(self, problem_name, output_dir, lang='', model='codex'):
        problem = Problem(problem_name)
        gen = problem.generate_func
        oracle = problem.oracle_func
        successes = {}

        signal.signal(signal.SIGALRM, self._sigalarm_handler)

        report_rows = []

        for text_, vars, index in gen(with_inputs=True, lang=lang):
            print(vars, end='', flush=True)
            report_row = vars.copy()

            print((Path(output_dir) / model / lang / problem_name / str(index)))
            files = (Path(output_dir) / model / lang / problem_name / str(index)).glob("*.py")
            input_path = Path('input') / model / lang / problem_name / f"{index}.txt"
            outputs = []
            expected = oracle(vars)

            result_str = ''
            result_emojis = ''

            for f in files:
                print(str(f))
                try:
                    actual = self._run_python(problem, f, vars, lang, model)
                    success = problem.is_output_equal(actual, expected)

                    if success:
                        print(EMOJI_PASS, end='')
                        result_str += 'p'
                        result_emojis += EMOJI_PASS
                    else:
                        print(EMOJI_FAIL, end='')
                        print("ACTUAL:", repr(actual))
                        print("EXPECTED:", repr(expected))
                        print()
                        result_str += 'f'
                        result_emojis += EMOJI_FAIL
                        report_row['expected'] = repr(expected)
                        report_row['actual'] = repr(actual)

                    outputs.append(actual)

                except ExecutionError as e:
                    success = False
                    result_str += 'e'
                    result_emojis += EMOJI_SYNTAX_ERROR
                    print(EMOJI_SYNTAX_ERROR, end='')
                    print(e)
                except TimeoutError as e:
                    success = False
                    result_str += 't'
                    result_emojis += EMOJI_TIMEOUT
                    print(EMOJI_TIMEOUT, end='')
                    print(e)


                for k, v in vars.items():
                    successes.setdefault((k, str(v)), []).append(success)

            report_row['result'] = result_str
            report_row['result_emojis'] = result_emojis
            # report_row['model_output'] = str(f)
            report_row['model_input'] = str(input_path)

            print()

            report_rows.append(report_row)

        print("Margin frequencies of success:")

        df = pd.DataFrame(report_rows)
        reports_dir = Path('reports') / model / lang
        reports_dir.mkdir(exist_ok=True)
        df.to_csv(reports_dir / f"report_{problem_name}.csv", index=False)

        success_rates = {k:mean([1.0 if e else 0 for e in v]) for k, v in successes.items()}
        success_rows = []
        for k, v in sorted(success_rates.items(), key=lambda i: i[1]):
            print(f"{k[0]}={k[1]}:", v)
            success_rows.append({'var': k[0], 'val': k[1], 'success_rate': v})

        df_rates = pd.DataFrame(success_rows)
        df_rates.to_csv(reports_dir / f"report_vars_{problem_name}.csv", index=False)


if __name__ == "__main__":
    fire.Fire(Main)
