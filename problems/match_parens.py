from multiprocessing.sharedctypes import Value
from problems.default import default_generate



NAMES = {
    '(': 'parentheses',
    '{': 'braces',
    '[': 'brackets',
    '<': 'brackets'
}

CLOSE = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

ORIGIN = 'humaneval'

INPUTS = [
    [['()(', ')']],
    [[')', ')']],
    [['(()(())', '())())']],
    [[')())', '(()()(']],
    [['(())))', '(()())((']],
    [['()', '())']],
    [['(()(', '()))()']],
    [['((((', '((())']],
    [[')(()', '(()(']],
    [[')(', ')(']],
    [['(', ')']],
    [[')', '(']]
]

def inputs(vars):
    def sub(s):
        return s.replace('(', vars['open']).replace(')', CLOSE[vars['open']])


    return [[[sub(j) for j in i[0]]] for i in INPUTS]


TARGET = lambda l, v: f"match_{NAMES[v['open']]}"

TEXT = """
def match_{name}(lst):
    '''
    You are given a list of two strings, both strings consist of open
    {name} '{open}' or close {name} '{close}' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all {name} in S
    are balanced. For example: the string '{open}{open}{close}{close}{open}{close}' is good, while the string
    '{open}{close}{close}' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['{open}{close}{open}', '{close}']) == 'Yes'
    match_parens(['{close}', '{close}']) == 'No'
    '''
"""

GRID = {
    'open': ['(', '{', '[', '<'],
}

def oracle_(input, open):
    def check(s):
        val = 0
        for i in s:
            if i == open:
                val = val + 1
            elif i == CLOSE[open]:
                val = val - 1
            else:
                raise ValueError(f"invalid char '{i}'")
            if val < 0:
                return False
        return True if val == 0 else False

    s1 = input[0] + input[1]
    s2 = input[1] + input[0]
    return 'Yes' if check(s1) or check(s2) else 'No'

def oracle(vars, input):
    return oracle_(input[0], vars['open'])

def render(**vars):
    vars['name'] = NAMES[vars['open']]
    vars['close'] = CLOSE[vars['open']]
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, inputs, render, *args, **kwargs)
