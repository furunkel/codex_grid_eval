from problems.default import default_generate
import re

TARGET = 'string_sequence'
INPUTS = list(range(100))
ORIGIN = "humaneval"

TEXT = """
def string_sequence(n: int) -> str:
    \"\"\" Return a string containing {delim}-delimited numbers starting from 0 upto n {inclusive_str}.
    >>> string_sequence({example_input})
    '{example_output}'
    \"\"\"
"""

DELIM_MAP = {
    'space': ' ',
    'comma': ', ',
    'semicolon': '; ',
    'hash': '#',
    'number sign': '#',
    'tab': '\t',
    'vertical line': '|'
}

GRID = {
    'inclusive': [True, False],
    'delim': ['space', 'comma', 'semicolon', 'hash', 'number sign', 'tab', 'vertical line'],
    'example_input': [1, 100, 500]
}

def is_output_equal(a, b):
    if a is None or b is None: return False
    def normalize(x):
        # allow space around delimiter
        x = re.sub(r' +([^ ]+) +', r'\1', x)

        # fuse multiple spaces
        x = re.sub(r' +', r' ', x)
        return x

    a = normalize(a)
    b = normalize(b)
    return a == b

def oracle_(input, inclusive, delim):
    if inclusive:
        n = input + 1
    else:
        n = input

    return DELIM_MAP[delim].join([str(x) for x in range(n)])

def oracle(vars):
    return oracle_(**dict((k, vars[k]) for k in ('input', 'inclusive', 'delim')))

def render(**vars):
    vars['inclusive_str'] = 'inclusive' if vars['inclusive'] else 'exclusive'
    vars['example_output'] = oracle_(input=vars['example_input'], inclusive=vars['inclusive'], delim=vars['delim'])
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, **kwargs)
