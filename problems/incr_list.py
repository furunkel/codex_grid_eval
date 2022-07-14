from problems.default import default_generate
from math import gcd as gcd
from itertools import product

INPUTS = [[[]], [[3, 2, 1]],
         [[5, 2, 5, 2, 3, 3, 9, 0, 123]]]

TARGET = "{op}_list"
ORIGIN = 'humaneval'

OP_TEXT = {
    'incr': 'incremented',
    'decr': 'decremented'
}

TEXT = """
def {op}_list(l: list):
    \"\"\"Return list with elements {op_text} by {step}.
    >>> {op}_list({example_input})
    {example_output}
    \"\"\"
"""

GRID = {
    'op': ['incr', 'decr'],
    'step': [0, 1, 2, 100, 9999, 3829893478785784890248],
    'example_input': [[1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123]]
}

def oracle_(input, op, step):
    result = []
    for i in input:
        if op == 'incr':
            result.append(i + step)
        elif op == 'decr':
            result.append(i - step)
    return result

def oracle(vars, input):
    return oracle_(input[0], vars['op'], vars['step'])

def render(**vars):
    vars['example_output'] = oracle_(vars['example_input'], vars['op'], vars['step'])
    vars['op_text'] = OP_TEXT[vars['op']]
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, **kwargs)
