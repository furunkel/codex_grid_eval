from problems.default import default_generate
from math import gcd as gcd
import re

INPUTS = ["aab_cbbbc", "AAB_CBBC",
          "aab__cbbbc", "AAB__CBBC",
          "aab______cbbbc", "AAB______CBBC",
          "aab?cbbbc", "AAB?CBBC",
          "aab+cbbbc", "AAB+CBBC",
          "aab-cbbbc", "AAB-CBBC",
          "aab?cbbbc", "AAB?CBBC"]

ORIGIN = "mbpp"
TARGET = "joined_sequence"
TEST_IMPORTS = ['re']

TEXT = """
def joined_sequence(text):
    \"\"\"
    Write a function to that returns {pos_ret} if the input string contains sequences of {case} letters joined with {sep} and {neg_ret} otherwise.
    \"\"\"
"""

GRID = {
    'pos_ret': [True, False],
    'neg_ret': [True, False],
    'sep': ['an underscore', 'two underscores', 'six underscores', 'a minus', 'a plus', 'a dash', 'a question mark'],
    'case': ['uppercase', 'lowercase']
}

def filter(vars):
    if vars['pos_ret'] == vars['neg_ret']: return False
    return True

SEP_CHARS = {
    'an underscore': '_',
    'two underscores': '__',
    'six underscores': '______',
    'a minus': '-',
    'a plus': r'\+',
    'a dash': '-',
    'a question mark': r'\?'
}

def oracle_(input, pos_ret, neg_ret, sep, case):
    if case == 'uppercase':
        char_re = r"[A-Z]"
    elif case == 'lowercase':
        char_re = r"[a-z]"
    else:
        raise ValueError('invalid case')

    sep_char = SEP_CHARS[sep]

    patterns = rf'^{char_re}+{sep_char}{char_re}+$'
    if re.search(patterns, input):
        return pos_ret
    else:
        return neg_ret

def oracle(vars):
    return oracle_(vars['input'], vars['pos_ret'], vars['neg_ret'], vars['sep'], vars['case'])

def render(**vars):
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render,  *args, filter_func=filter, **kwargs)
