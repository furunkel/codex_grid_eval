import subprocess
from xml.dom import SYNTAX_ERR
import openai
import itertools
from tqdm import tqdm
import fire
import time
from pathlib import Path
from math import prod
from statistics import mean

EMOJI_PASS = "\u2705"  
EMOJI_FAIL = "\u274c"
EMOJI_SYNTAX_ERROR = "\U0001F480"


def oracle(factors, below, agg):
    assert agg in ['sum', 'product']
    nums = []
    for i in range(1, below):
        for factor in factors:
            if i % factor == 0: 
                nums.append(i)
                break
    return nums, sum(nums) if agg == 'sum' else prod(nums)

TEXT = """If we list all the natural numbers below {example_below} that are multiples of {factors_text}, we get {example_numbers}. The {agg} of these multiples is {example_sum}.
Find the {agg} of all the multiples of {factors_text} below {below}."""

VARIABLES = [
    {'example_below': 10, 'factors': [3, 5], 'below': 1000},
    {'example_below': 10, 'factors': [5, 3], 'below': 1000},

    {'example_below': 100, 'factors': [3, 5], 'below': 1000},
    {'example_below': 100, 'factors': [5, 3], 'below': 1000},

    {'example_below': 10, 'factors': [3, 5, 7], 'below': 1000},
    {'example_below': 10, 'factors': [7, 5, 3], 'below': 1000},
    {'example_below': 10, 'factors': [5, 7, 3], 'below': 1000},
]

GRID = {
    'example_below': [10, 15, 5],
    'factors': [[3, 5], [5, 3], [2, 5], [2,3,5], [5,3,2], [13, 17], [5,7,9], [2,9]],
    'below': [100, 124, 197, 200, 500, 600, 1000],
    'agg': ['sum', 'product']
}

def int_list_to_str(lst, conjunction = 'and'):
    return f"{', '.join([str(i) for i in lst[:-1]])} {conjunction} {lst[-1]}"

def render(**vars):
    example_nums, example_sum = oracle(vars['factors'], vars['example_below'], vars['agg'])
    if not example_nums: return None

    vars['factors_text'] = int_list_to_str(vars['factors'], 'or')
    vars['example_numbers'] = int_list_to_str(example_nums)
    vars['example_sum'] = example_sum

    return TEXT.format(**vars)

def to_comment(text):
    #return "\n".join(["# " + l for l in text.splitlines()] + ["# Use Python"])
    return '"""' + text + '"""'


def save(index, input, outputs):
    input_dir = Path('./inputs')
    input_dir.mkdir(exist_ok=True, parents=True)

    (input_dir / f"{index}.txt").write_text(input)

    output_dir = Path('./outputs') / str(index)
    output_dir.mkdir(exist_ok=True, parents=True)

    for i, o in enumerate(outputs):
        (output_dir / f"{i}.py").write_text(o)


class Main:
    def eval(self, temperature=0, top_p=1, n=1, max_tokens=512):
        for index, vals in enumerate(tqdm(list(itertools.product(*GRID.values())))):
            vars = dict(zip(GRID.keys(), vals))
            text = render(**vars)
            if not text:
                continue
            input = to_comment(text)

            print(input)
            print()

            while True:
                try:
                    e = openai.Completion.create(engine='code-davinci-002',
                                    prompt=input, temperature=temperature, top_p=top_p,
                                    n=n, max_tokens=max_tokens)
                    outputs = list(set(filter(None, [c.text for c in e.choices if 'text' in c])))
                    break
                except openai.error.RateLimitError:
                    print("Rate limit reached. Retrying in 10 seconds...")
                    time.sleep(10)
                except openai.error.InvalidRequestError:
                    outputs = []
                    break

            print(len(outputs))
            save(index, input, outputs)

    def test(self, output_dir):
        successes = {}

        for index, vals in enumerate(list(itertools.product(*GRID.values()))):
            vars = dict(zip(GRID.keys(), vals))
            print(vars, end='')
            files = (Path(output_dir) / str(index)).glob("*.py")
            outputs = []

            _, expected_sum = oracle(vars['factors'], vars['below'], vars['agg'])

            for f in files:
                try:
                    output = subprocess.run(['python', str(f)], check=True, capture_output=True)

                    try:
                        actual_sum = int(output.stdout)
                    except ValueError:
                        actual_sum = None

                    success = actual_sum == expected_sum

                    if success:
                        print(EMOJI_PASS, end='')
                    else:
                        print(EMOJI_FAIL, end='')
                        # print("ACTUAL:", actual_sum)
                        # print("EXPECTED:", expected_sum)
                        # print()

                    for k, v in vars.items():
                        successes.setdefault(f"{k}={v}", []).append(success)

                except subprocess.CalledProcessError:
                    print(SYNTAX_ERR, end='')

                outputs.append(output.stdout)
            print()

        print("Margin frequencies of success:")

        success_rates = {k:mean([1.0 if e else 0 for e in v]) for k, v in successes.items()}
        for k, v in sorted(success_rates.items(), key=lambda i: i[1]):
            print(f"{k}:", v)

            

if __name__ == "__main__":
    fire.Fire(Main)
