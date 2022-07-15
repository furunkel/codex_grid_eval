from problems.default import default_generate
from math import gcd as gcd
from itertools import product

INPUTS = [[[1, 3, 5, 0]], [[2, 4, -5, 3, 9, 7]],
         [[-1, -2, 3, 4, 5, 7, 8]],
         [[-16, 1, 2, 3, 4, 5, 6, 8, 8]],
         [[-100, 0, 2, 80, 20, 10, 10, 5, 5, 5, 5, 2, 2, 2, 1, 1, 1, 1]],
         [[10, 10, 10, 10, 10, 10, 10, 10, 20, 30, 40]],
         [[-9, -8, -7, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2]]]

COUNT_NAME = {
    2: 'doubles',
    3: 'triples',
    4: 'quadruples',
    5: 'quintuples',
    8: 'octuples',
    10: 'decuples'
}

ORIGIN = "humaneval"

SUM_TO_TEXT = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    5: 'five',
    100: 'hundred'
}

TARGET = lambda lang, vars: f"{COUNT_NAME[vars['count']]}_sum_to_{SUM_TO_TEXT[vars['sum_num']]}"

TEXT = """
def {count_name}_sum_to_{sum_text}(l: list):
    \"\"\"
    {count_name}_sum_to_{sum_text} takes a list of integers as an input.
    it returns True if there are {count} distinct elements in the list that
    sum to {sum_text}, and False otherwise.

    >>> {count_name}_sum_to_{sum_text}({example_input})
    {example_output}
    \"\"\"
"""

GRID = {
    'sum_num': [0, 1, 2, 3, 5, 100],
    'count': [2, 3, 4, 5, 8, 10],
    'example_input': [[1, 3, 5, 0], [1, 3, -2, 1, 5, 8], [1, 2, -3, 7, 2, 7], [1]]
}

def oracle_(input, count, sum_num):
    if count == 5:
        # too slow otherwise
        l = len(input)
        for i1 in range(l):
            for i2 in range(i1 + 1, l):
                for i3 in range(i2 + 1, l):
                    for i4 in range(i3 + 1, l):
                        for i5 in range(i4 + 1, l):
                            if input[i1] + input[i2] + input[i3] + input[i4] + input[i5] == sum_num:
                                return True

    elif count == 8:
        l = len(input)
        for i1 in range(l):
            for i2 in range(i1 + 1, l):
                for i3 in range(i2 + 1, l):
                    for i4 in range(i3 + 1, l):
                        for i5 in range(i4 + 1, l):
                            for i6 in range(i5 + 1, l):
                                for i7 in range(i6 + 1, l):
                                    for i8 in range(i7 + 1, l):
                                        if input[i1] + input[i2] + input[i3] + input[i4] + input[i5] + input[i6] + input[i7] + input[i8] == sum_num:
                                            return True
    elif count == 10:
        l = len(input)
        for i1 in range(l):
            for i2 in range(i1 + 1, l):
                for i3 in range(i2 + 1, l):
                    for i4 in range(i3 + 1, l):
                        for i5 in range(i4 + 1, l):
                            for i6 in range(i5 + 1, l):
                                for i7 in range(i6 + 1, l):
                                    for i8 in range(i7 + 1, l):
                                        for i9 in range(i8 + 1, l):
                                            for i10 in range(i9 + 1, l):
                                                if input[i1] + input[i2] + input[i3] + input[i4] + input[i5] + input[i6] + input[i7] + input[i8] + input[i9] + input[i10] == sum_num:
                                                    return True
    else:
        for idx in product(*([list(range(len(input)))] * count)):
            if all(idx[i] < idx[i + 1] for i in range(count - 1)) and sum(input[idx[i]] for i in range(count)) == sum_num:
                return True
    return False

    return False

def oracle(vars, input):
    return oracle_(input[0], vars['count'], vars['sum_num'])

def render(**vars):
    vars['sum_text'] = SUM_TO_TEXT[vars['sum_num']]
    vars['count_name'] = COUNT_NAME[vars['count']]
    vars['example_output'] = oracle_(vars['example_input'], vars['count'], vars['sum_num'])
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, **kwargs)
