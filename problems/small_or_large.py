from problems.default import default_generate

TARGET = 'small_or_large'
INPUTS = [-100,
          -1,
          0,
          10,
          100,
          1000,
          2000,
          1_000_000
]
ORIGIN = 'gpsbs'

TEXT = """
def small_or_large(n):
    \"\"\"
        Given an integer n, return "{small_ret}" if n < {small_limit} and "{large_ret}" if n >= {large_limit} (and {default_ret} if {small_limit} <= n < {large_limit}).
    \"\"\"
"""

def filter(vars):
    if vars['small_limit'] + 1 >= vars['large_limit']: return False
    if vars['small_ret'] == vars['large_ret']: return False
    return True

GRID = {
    'small_ret': ["small", "large", "mouse"],
    'large_ret': ["large", "small", "house"],
    'default_ret': [None, "None", "neither"],
    'small_limit': [-100, 2, 10, 1000],
    'large_limit': [-1, 2, 15, 2000],
}

def oracle_(input, small_limit, large_limit, small_ret, large_ret, default_ret):
    if input < small_limit: return small_ret
    if input >= large_limit: return large_ret
    return default_ret

def oracle(vars, input):
    return oracle_(input=input, **dict((k, vars[k]) for k in ('small_limit', 'large_limit', 'small_ret', 'large_ret', 'default_ret')))

def render(**vars):
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, filter_func=filter, **kwargs)
