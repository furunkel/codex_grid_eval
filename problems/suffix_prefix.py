from problems.default import default_generate

TARGET = 'all_{op}'
INPUTS = ["", "asdfgh", "WWW"]
TEST_IMPORTS = [('typing', 'List'), 're']
ORIGIN = "humaneval"

TEXT = """
def all_{op}(string: str) -> List[str]:
    \"\"\" Return list of all prefixes {order_str} of the input string
    >>> all_{op}('{example_input}')
    {example_output}
    \"\"\"
"""

ORDER_STR = {
    'shortest_first': 'from shortest to longest',
    'longest_first': 'from longest to shortest'
}

# ['a', 'ab', 'abc']
GRID = {
    'op': ['prefixes', 'suffixes'],
    'example_input': ['abc', 'xyz', 'suffix', 'prefix', 'reverse the result!!!', '12345678'],
    'order': ['longest_first', 'shortest_first']
}

def oracle_(input, op, order):
    result = []

    for i in range(len(input)):
        if op == 'prefixes':
            result.append(input[:i+1])
        elif op == 'suffixes':
            result.append(input[-i-1:])
        else:
            raise ValueError(f'invalid op {op}')

    if order == 'shortest_first':
        pass
    elif order == 'longest_first':
        result.reverse()
    else:
        raise ValueError(f'invalid order {order}')

    return result

def oracle(vars, input):
    return oracle_(input=input, **dict((k, vars[k]) for k in ('op', 'order')))

def render(**vars):
    vars['order_str'] = ORDER_STR[vars['order']]
    vars['example_output'] = oracle_(input=vars['example_input'], op=vars['op'], order=vars['order'])
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, **kwargs)
