from problems.default import default_generate
from math import prod

def oracle_(factors, below, agg):
    assert agg in ['sum', 'product']
    nums = []
    for i in range(1, below):
        for factor in factors:
            if i % factor == 0: 
                nums.append(i)
                break
    return nums, sum(nums) if agg == 'sum' else prod(nums)

def oracle(vars):
    _, r = oracle_(vars['factors'], vars['below'], vars['agg'])
    return str(r)

TEXT = """If we list all the natural numbers below {example_below} that are multiples of {factors_text}, we get {example_numbers}. The {agg} of these multiples is {example_sum}.
Find the {agg} of all the multiples of {factors_text} below {below}."""

GRID = {
    'example_below': [10, 15, 5],
    'factors': [[3, 5], [5, 3], [2, 5], [2,3,5], [5,3,2], [13, 17], [5,7,9], [2,9]],
    'below': [100, 124, 197, 200, 500, 600, 1000],
    'agg': ['sum', 'product']
}

def int_list_to_str(lst, conjunction = 'and'):
    return f"{', '.join([str(i) for i in lst[:-1]])} {conjunction} {lst[-1]}"

def render(**vars):
    example_nums, example_sum = oracle_(vars['factors'], vars['example_below'], vars['agg'])
    if not example_nums: return None

    vars['factors_text'] = int_list_to_str(vars['factors'], 'or')
    vars['example_numbers'] = int_list_to_str(example_nums)
    vars['example_sum'] = example_sum

    return TEXT.format(**vars)


def generate(*args, **kwargs):
    default_generate(GRID, [], render, *args, **kwargs)