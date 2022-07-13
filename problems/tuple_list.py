from random import randint
from problems.default import default_generate
from math import gcd as gcd
from operator import itemgetter 

def gen_rand_inputs(n):
    return [[tuple(randint(0, 100) for j in range(12)) for i in range(1, n + 1)]]

INPUTS = [gen_rand_inputs(i) for i in range(1, 10)]

ORIGIN = "mbpp"
TARGET = "joined_sequence"
TEST_IMPORTS = ['re']

TARGET = '{func_name}'

TEXT = """
def {func_name}(lst):
    \"\"\"
    Given a list of tuples, write a function that returns the {ret_index} value of the tuple with the {cmp} {cmp_index} value.
    \"\"\"
"""

GRID = {
    'ret_index': ['first', 'second', 'third', 'twelfth', 'eleventh', 'last'],
    'cmp_index': ['first', 'second', 'third', 'twelfth', 'eleventh', 'last'],
    'cmp': ['smallest', 'largest'],
    'func_name': ['extract_value', 'tuple_extract', 'f', 'some_func', 'fibonacci', 'min_max']
}

def filter(vars):
    # if vars['ret_index'] == vars['cmp_index']: return False
    return True

INDEX_MAP = {
    'first': 0,
    'second': 1,
    'third': 2,
    'eleventh': 10,
    'twelfth': 11,
    'last': -1,
}

def oracle_(input, ret_index, cmp, cmp_index):
    if cmp == 'smallest':
        cmp_func = min
    elif cmp == 'largest':
        cmp_func = max
    else:
        raise ValueError('invalid cmp')

    res = cmp_func(input, key = itemgetter(INDEX_MAP[cmp_index]))[INDEX_MAP[ret_index]]
    return (res) 

def oracle(vars):
    return oracle_(vars['input'][0], vars['ret_index'], vars['cmp'], vars['cmp_index'])

def render(**vars):
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render,  *args, filter_func=filter, **kwargs)
