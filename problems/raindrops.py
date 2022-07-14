from problems.default import default_generate
from math import gcd as gcd

INPUTS = list(range(1, 128))
TARGET = "raindrops"
ORIGIN = 'exercism'

TEXT = """
def raindrops(num):
    \"\"\"
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has {factor1} as a factor, add '{factor1_result}' to the result.
    has {factor2} as a factor, add '{factor2_result}' to the result.
    has {factor3} as a factor, add '{factor3_result}' to the result.
    does not have any of {factor1}, {factor2}, or {factor3} as a factor, the result should be the digits of the number as a string.

    Examples:
    {factor3_example} has {factor3} as a factor, but not {factor1} or {factor2}, so the result would be "{factor3_result}".
    {factor1_2_example} has both {factor1} and {factor2} as factors, but not {factor3}, so the result would be "{factor1_result}{factor2_result}".
    {factor_none_example} is not factored by {factor1}, {factor2}, or {factor3}, so the result would be "{factor_none_example}".
    \"\"\"
"""

def filter(vars):
    # all factors should be different
    f1, f2, f3 = vars['factor1'], vars['factor2'], vars['factor3']

    # factors should be relative prime
    if gcd(f1, f2) != 1: return False
    if gcd(f1, f3) != 1: return False
    if gcd(f2, f3) != 1: return False

    if len({vars['factor1_result'], vars['factor2_result'], vars['factor3_result']}) != 3: return False
    return True

GRID = {
    'factor1': [3, 11, 13],
    'factor2': [5, 3, 11],
    'factor3': [7, 5, 11],
    'factor1_result': ['Pling', 'Plang', 'Fizz'],
    'factor2_result': ['Plang', 'Pling', 'Buzz'],
    'factor3_result': ['Plong', 'Plang', 'Buzz'],
}

def find_example_factor3(factor1, factor2, factor3):
    for i in range(2 * factor3, factor3 * 1000, factor3):
        if i % factor1 != 0 and i % factor2 != 0: return i
    raise RuntimeError(f"no factor found for {factor1}, {factor2}, {factor3}")

def find_example_factor1_2(factor1, factor2, factor3):
    min_f = min(factor1, factor2)
    for i in range(2 * min_f, min_f * 1000, min_f):
        if i % factor1 == 0 and i % factor2 == 0 and i % factor3 != 0: return i
    raise RuntimeError(f"no factor found for {factor1}, {factor2}, {factor3}")

def find_example_factor_none(factor1, factor2, factor3):
    for i in range(2, 10_000_000):
        if i % factor1 != 0 and i % factor2 != 0 and i % factor3 != 0: return i
    raise RuntimeError(f"no factor found for {factor1}, {factor2}, {factor3}")


def oracle_(input, factor1, factor2, factor3, factor1_result, factor2_result, factor3_result):
    result = ""
    if input % factor1 == 0:
        result += factor1_result
    if input % factor2 == 0:
        result += factor2_result
    if input % factor3 == 0:
        result += factor3_result
    if not result:
        result = str(input)
    return result

def oracle(vars, input):
    return oracle_(input=input, **dict((k, vars[k]) for k in ('factor1', 'factor2', 'factor3', 'factor1_result', 'factor2_result', 'factor3_result')))

def render(**vars):
    vars['factor3_example'] = find_example_factor3(vars['factor1'], vars['factor2'], vars['factor3'])
    vars['factor1_2_example'] = find_example_factor1_2(vars['factor1'], vars['factor2'], vars['factor3'])
    vars['factor_none_example'] = find_example_factor_none(vars['factor1'], vars['factor2'], vars['factor3'])
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, filter_func=filter, **kwargs)
