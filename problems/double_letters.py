from problems.default import default_generate
from math import gcd as gcd
import re

INPUTS = [
    'aaaAB1!1kf!kd3?f3fk?lk3',
    '???!!!!ABCdefg1234aaaee',
    'A?',
    '?',
    '!!!!!',
    'AAAaaaaaAAAA',
    '1A2B3C!',
]
TARGET = "double_letters"
ORIGIN = 'gpsbs' # https://thelmuth.github.io/GECCO_2015_Benchmarks_Materials/

TEXT = """
def double_letters(string):
    \"\"\"
    Given a string, return the string, doubling every {double_class} character, and tripling every {triple_class}.
    All other characters should be output a single time each.
    \"\"\"
"""

CLASSES = ['letter', 'number', 'upper-case letter', 'lower-case letter', 'exclamation point',
           'question mark', 'vowel (lower-case or upper-case)', 'consonant (lower-case or upper-case)']

GRID = {
    'double_class': CLASSES,
    'triple_class': CLASSES,
}

CLASS_MAP = {
    'letter': r'[A-Za-z]',
    'number': r'[0-9]',
    'upper-case letter': r'[A-Z]',
    'lower-case letter': r'[a-z]',
    'exclamation point': '!',
    'question mark': r'\?',
    'vowel (lower-case or upper-case)': r'[aeiouAEIOU]',
    'consonant (lower-case or upper-case)': r'[bcdfghjklmnpqrstvwxysBCDFGHJKLMNPQRSTVWXYS]',
}

CONFLICT_CLASSES = [
    ('letter', 'upper-case letter'),
    ('letter', 'lower-case letter'),
    ('letter', 'vowel (lower-case or upper-case)'),
    ('letter', 'consonant (lower-case or upper-case)'),
    ('upper-case letter', 'vowel (lower-case or upper-case)'),
    ('upper-case letter', 'consonant (lower-case or upper-case)'),
    ('lower-case letter', 'vowel (lower-case or upper-case)'),
    ('lower-case letter', 'consonant (lower-case or upper-case)'),
]

def filter(vars):
    dc, tc = vars['double_class'], vars['triple_class']

    if (dc, tc) in CONFLICT_CLASSES or (tc, dc) in CONFLICT_CLASSES: return False

    if vars['double_class'] == vars['triple_class']: return False
    return True

def oracle_(input, double_class, triple_class):
    result = ""
    for c in input:
        if re.match(CLASS_MAP[double_class], c):
            result += c * 2
        elif re.match(CLASS_MAP[triple_class], c):
            result += c * 3
        else:
            result += c
    return result

def oracle(vars):
    return oracle_(**dict((k, vars[k]) for k in ('input', 'double_class', 'triple_class')))

def render(**vars):
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, filter_func=filter, **kwargs)
