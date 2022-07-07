from problems.default import default_generate
from math import gcd as gcd

INPUTS = [50, 78, 79, 100, 200, 4000, 10000, 100000]
TARGET = "fizz_buzz"
ORIGIN = 'humaneval'

TEXT = """
def fizz_buzz(n:int):
    \"\"\"Return the number of times the digit {digit} appears in integers less than n which are divisible by {factor2} or {factor3}.
    >>> fizz_buzz({example_input})
    {example_output}
    \"\"\"
"""

GRID = {
    'digit': [7, 4, 3, 1],
    'factor2': [11, 13, 7, 1837],
    'factor3': [13, 11, 3819],
    'example_input': [50, 78, 3298]
}

def filter(vars):
    # all factors should be different
    f1, f2 = vars['factor2'], vars['factor3']
    # factors should be relative prime
    if gcd(f1, f2) != 1: return False
    return True

def oracle_(input, digit, factor2, factor3):
    ns = []
    for i in range(input):
        if i % factor2 == 0 or i % factor3 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == str(digit))
    return ans

def oracle(vars):
    return oracle_(**dict((k, vars[k]) for k in ('input', 'digit', 'factor2', 'factor3')))

def render(**vars):
    vars['example_output'] = oracle_(vars['example_input'], vars['digit'], vars['factor2'], vars['factor3'])
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, filter_func=filter, **kwargs)
