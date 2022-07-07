import itertools
from math import sqrt
from problems.default import default_generate

FUNCS = {
    '+': lambda x: x + x,
    '-': lambda x: x - x,
    '*': lambda x: x * x,
    '**2': lambda x: x**2,
    'sqrt': lambda x: sqrt(x),
}
ORIGIN = '100+' # https://github.com/zhiwehu/Python-programming-exercises

FLOAT_FUNCS = {'sqrt'}

FUNC_I = {
    '+': 'i + i',
    '-': 'i - i',
    '*': 'i * i',
    '**2': 'i**2',
    'sqrt': 'sqrt(i)',
}

TEXT = """
\"\"\"
    With a given {number_type} number n, write a program to generate a dictionary that contains (i, {func_i}) such that i is a {number_type} number between 1 and n (both included) and then the program should print the dictionary.
    {example}
\"\"\"
"""

EXAMPLE = """
Suppose the following input is supplied to the program:
{example_len}
Then, the output should be:
{example_dict}

Hint:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

GRID = {
    'number_type': ['integral'], #, 'float', 'decimal'],
    'func': ['+', '-', '*', 'sqrt', '**2', ],
    'example_len': [0, 1, 3, 5, 8, 100],
}

INPUTS = [1, 2, 5, 9, 10, 100]

def oracle_(length, func):
    dct = {}
    for i in range(1, length + 1):
        dct[i] = FUNCS[func](i)
    return dct

def oracle(vars):
    return str(oracle_(vars['input'], vars['func']))

def render(**vars):
    example_dict = oracle_(vars['example_len'], vars['func'])
    vars['func_i'] = FUNC_I[vars['func']]

    # if vars['func'] in FLOAT_FUNCS:
    #     vars['number_type'] = 'decimal'

    if vars['example_len'] > 0:
        vars['example'] = EXAMPLE.format(example_len=vars['example_len'], example_dict={k:round(v, 3) for k, v in example_dict.items()})
    else:
        vars['example'] = ''
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, **kwargs)
