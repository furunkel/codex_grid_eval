from problems.default import default_generate
from math import gcd as gcd

INPUTS = list(range(1, 128))
TARGET = "fizzbuzz"

TEXT = """
def fizzbuzz(num):
    \"\"\"
    Given a number, this function returns
        "Fizz" for multiples of {factor1} (instead of the number),
        "Buzz" for multiples of {factor2} (instead of the number),
        "FizzBuzz" for multiples of both {factor1} and {factor2}  (instead of the number),
        the number itself otherwise.
    \"\"\"
"""

GRID = {
    'factor1': [3, 4, 144546, 'three', 'five', 'eleven', 'seventeen', 'ninety-nine'],
    'factor2': [5, 3, 11, 17, 23, 4948938, 'twenty-three', 'a hundred and seventeen'],
}

FACTOR_MAP = {
    'three': 3,
    'five': 5,
    'eleven': 11,
    'seventeen': 17,
    'twenty-three': 23,
    'ninety-nine': 99,
    'a hundred and seventeen': 117
}

def factor_to_int(factor):
    return FACTOR_MAP.get(factor, factor)

def filter(vars):
    # all factors should be different
    f1, f2 = factor_to_int(vars['factor1']), factor_to_int(vars['factor2'])
    # factors should be relative prime
    if gcd(f1, f2) != 1: return False
    return True

def oracle_(input, factor1, factor2):
    result = ""
    if input % factor_to_int(factor1) == 0 and input % factor_to_int(factor2) == 0:
        result = 'FizzBuzz'
    elif input % factor_to_int(factor1) == 0:
        result += 'Fizz'
    elif input % factor_to_int(factor2) == 0:
        result += 'Buzz'
    else:
        result = input
    return result

def oracle(vars):
    return oracle_(**dict((k, vars[k]) for k in ('input', 'factor1', 'factor2')))

def render(**vars):
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, filter_func=filter, **kwargs)
