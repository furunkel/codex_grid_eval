from random import randint
from problems.default import default_generate
from math import gcd as gcd
from operator import itemgetter 

INPUTS = [
    [0, 0b1],
    [0, 0b11],
    [0, 0b111],
    [0, 0b11111],
    [0, 0b11111111111],
    [0, 0b111111111111111],
    [0, 0b11111111111111111111111111111],
    [0b1, 0b1],
    [0b1, 0b11],
    [0b010, 0b111],
    [0b10101, 0b11111],
    [0b101010101, 0b11111111111],
    [0b101010101110101, 0b111111111111111],
    [0b111111111111111111, 0b11111111111111111111111111111],
 ]

ORIGIN = "mbpp"
TARGET = "bit_diff"

TEXT = """
def bit_diff(a, b):
    \"\"\"
    Returns whether the two numbers differ at exactly {count_in_text} bit {position}.
    \"\"\"
"""

GRID = {
    'count': [0, 1, 2, 3, 4, 5, 6, 11, 15, 29],
    'word_count': [True, False]
}

NUMBER_MAP = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    11: 'eleven',
    15: 'fifteen',
    29: 'twenty-none'
}

def filter(vars):
    # if vars['ret_index'] == vars['cmp_index']: return False
    return True

def oracle_(a, b, count):
    return bin(a ^ b).count('1') == count

def oracle(vars):
    return oracle_(*vars['input'], vars['count'])

def render(**vars):
    if vars['word_count']:
        vars['count_in_text'] = NUMBER_MAP[vars['count']]
    else:
        vars['count_in_text'] = vars['count']

    vars['position'] = 'position' if vars['count'] == 1 else 'positions'
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render,  *args, filter_func=filter, **kwargs)
