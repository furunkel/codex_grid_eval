from dataclasses import dataclass
import subprocess

from numpy import isin
import openai
from tqdm import tqdm
import fire
from tree_sitter import Language, Parser

import time
from pathlib import Path
from math import prod
from statistics import mean
import textwrap
from types import ModuleType

EMOJI_PASS = "\u2705"  
EMOJI_FAIL = "\u274c"
EMOJI_SYNTAX_ERROR = "\U0001F480"

Language.build_library(
  'build/tree_sitter.so',
  [
    'vendor/tree-sitter-python'
  ]
)

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
        imports = [node_to_code(code_bytes, c[0]) for c in captures]
        out_code = "\n".join(imports) + "\n" + func
    else:
        out_code = None

    return out_code

def to_comment(text):
    #return "\n".join(["# " + l for l in text.splitlines()] + ["# Use Python"])
    return '"""' + text + '"""'

def save(problem_name, index, input, outputs):
    input_dir = Path('./inputs') / problem_name
    input_dir.mkdir(exist_ok=True, parents=True)

    (input_dir / f"{index}.txt").write_text(input)

    output_dir = Path('./outputs') / problem_name / str(index)
    output_dir.mkdir(exist_ok=True, parents=True)

    for i, o in enumerate(outputs):
        (output_dir / f"{i}.py").write_text(o)

@dataclass
class Problem:
    name: str

    def __post_init__(self):
        problems_mod = __import__(f'problems.{self.name}')
        self.mod = getattr(problems_mod, self.name)

    @property
    def generate_func(self):
        return getattr(self.mod, 'generate')
        
    @property
    def oracle_func(self):
        return getattr(self.mod, 'oracle')

    @property
    def run_func(self):
        return getattr(self.mod, 'run')

    @property
    def has_target(self):
        return hasattr(self.mod, 'TARGET')

    @property
    def target_name(self):
        return getattr(self.mod, 'TARGET')

    def is_output_equal(self, a, b):
        if hasattr(self.mod, 'is_output_equal'):
            return getattr(self.mod, 'is_output_equal')(a, b)
        else:
            return a == b

class Main:

    FAKE_INPUT_FUNC = """
      def input(*args):
          return {input}
    """

    def patch_python(self, code, input):
        return textwrap.dedent(self.FAKE_INPUT_FUNC.format(input=input)) + code

    def eval(self, problem_name, temperature=0, top_p=1, n=1, max_tokens=512, dry_run=False):
        problem = Problem(problem_name)
        gen = problem.generate_func
        for text, _vars, index in tqdm(list(gen())):
        # for index, vals in enumerate(tqdm(list(itertools.product(*GRID.values())))):
        #     vars = dict(zip(GRID.keys(), vals))
        #     text = render(**vars)
            if not text:
                continue
            if not problem.has_target:
                input = to_comment(text)
            else:
                input = text
            print(input)
            print()

            if not dry_run:
                while True:
                    try:
                        e = openai.Completion.create(engine='code-davinci-002',
                                        prompt=input, temperature=temperature, top_p=top_p,
                                        n=n, max_tokens=max_tokens, echo=problem.has_target)
                        outputs = list(set(filter(None, [c.text for c in e.choices if 'text' in c])))
                        break
                    except openai.error.RateLimitError:
                        print("Rate limit reached. Retrying in 10 seconds...")
                        time.sleep(10)
                    except openai.error.InvalidRequestError:
                        outputs = []
                        break
            else:
                outputs = []

            print(len(outputs))
            save(problem_name, index, input, outputs)

    def run_python(self, problem, f, vars):
        if problem.has_target:
            code = extract_first_func(f.read_text())
            exec_obj = compile(code, str(f), 'exec')
            module = ModuleType(str(f).replace('/', '.'))
            exec(exec_obj, module.__dict__)
            target = getattr(module, problem.target_name)
            input = vars['input']
            if not isinstance(input, list): input = [input]
            return target(*input)
            # mod = __import__(str(f).replace('/', '.'))
            # target = getattr(mod, target)
            # target(*vars['input'])
            # return problem.run_func(target, vars)
        else:
            code = self.patch_python(f.read_text(), vars['input'])
            print(code)
            output = subprocess.run(['python', '-c', code], check=True, capture_output=True, text=True)

            print(output.stdout)
            try:
                actual = output.stdout.strip() #.splitlines()[-1]
            except ValueError:
                actual = None

            return actual

    def test(self, problem_name, output_dir):
        problem = Problem(problem_name)
        gen = problem.generate_func
        oracle = problem.oracle_func
        successes = {}

        for text_, vars, index in gen(with_inputs=True):
            print(vars, end='', flush=True)
            files = (Path(output_dir) / problem_name / str(index)).glob("*.py")
            outputs = []
            expected = oracle(vars)

            for f in files:
                print(str(f))

                try:
                    actual = self.run_python(problem, f, vars)
                    success = problem.is_output_equal(actual, expected)

                    if success:
                        print(EMOJI_PASS, end='')
                    else:
                        print(EMOJI_FAIL, end='')
                        print("ACTUAL:", repr(actual))
                        print("EXPECTED:", repr(expected))
                        print()

                    for k, v in vars.items():
                        successes.setdefault(f"{k}={v}", []).append(success)

                    outputs.append(actual)

                except subprocess.CalledProcessError:
                    print(EMOJI_SYNTAX_ERROR, end='')

            print()

        print("Margin frequencies of success:")

        success_rates = {k:mean([1.0 if e else 0 for e in v]) for k, v in successes.items()}
        for k, v in sorted(success_rates.items(), key=lambda i: i[1]):
            print(f"{k}:", v)

            

if __name__ == "__main__":
    fire.Fire(Main)
