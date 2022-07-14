from problems.default import default_generate

TARGET = 'string_{op}'
INPUTS = [
    ['111000', '101010'],
    ['1', '1'],
    ['0', '0'],
    ['0101', '0000']
]
ORIGIN = "humaneval"

TEXT = """
from typing import List

def string_{op}(a: str, b: str) -> str:
    \"\"\" Input are two strings a and b consisting only of 1s and 0s.
    Perform binary {op_upper} on these inputs and return result also as a string.
    >>> string_{op}('010', '110')
    '{example_result}'
    \"\"\"
"""

GRID = {
    'op': ['xor', 'and', 'nand', 'or', 'nor', 'xnor', 'xand']
}

def filter(vars):
    return True

def oracle_(input, op):
    def exec_op(i, j):
        if op == 'xor':
            return '0' if i == j else '1'
        elif op == 'or':
            return '0' if (i == '0' and j == '0') else '1'
        elif op == 'nor':
            return '1' if (i == '0' and j == '0') else '0'
        elif op == 'and':
            return '0' if (i == '0' or j == '0') else '1'
        elif op == 'nand':
            return '1' if (i == '0' or j == '0') else '0'
        if op == 'xnor' or op == 'xand':
            return '1' if i == j else '0'
        else:
            raise ValueError("invalid op")

    return ''.join(exec_op(x, y) for x, y in zip(*input))

def oracle(vars, input):
    return oracle_(input=input, op=vars['op'])

def render(**vars):
    vars['op_upper'] = vars['op'].upper()
    vars['example_result'] = oracle_(['010', '110'], vars['op'])
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, filter_func=filter, **kwargs)
