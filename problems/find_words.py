from problems.default import default_generate
from math import gcd as gcd
import re

INPUTS = ["a " + "b" * 40, "aaa", "aaaaaa", "a" * 20 + " " + " b c d e",
          "c" * 20, "b bbb bbbbbb", "b bbb bbbbbbb", "Please move back to stream",
          "Jhingai wulu road Zone 3"]

ORIGIN = "mbpp"
TARGET = "find_char_long"
TEST_IMPORTS = ['re']

TEXT = """
def find_char_long(text):
    \"\"\"
    Finds all words which are {cond} {length} characters long in a string.
    \"\"\"
"""

GRID = {
    'length': [1, 3, 6, 20],
    'cond': ['at least', 'exactly', 'at most', 'not']
}

def oracle_(input, length, condition):
    words = re.split("\s+", input)
    result = []

    for word in words:
        if condition == 'at least': 
            if len(word) >= length: result.append(word)
        elif condition == 'exactly':
            if len(word) == length: result.append(word)
        elif condition == 'at most':
            if len(word) <= length: result.append(word)
        elif condition == 'not':
            if len(word) != length: result.append(word)
        else:
            raise ValueError("invalid condition")

    return result

def oracle(vars):
    return oracle_(vars['input'], vars['length'], vars['cond'])

def render(**vars):
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, **kwargs)
