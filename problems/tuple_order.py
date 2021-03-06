from problems.default import default_generate

INPUTS = [
    [3, 5],
    [7, 10],
    [0, 0],
    [1, 0],
    [0, 1],
    [100, 20],
]

ORIGIN = "hackerrank"
TARGET = "make_tuple"

TEXT = """
def make_tuple({var1_name}, {var2_name}):
    \"\"\"
    Given two integers {var1_name} and {var2_name}, return a tuple where:
    The {line_order1} element contains the {op1} of the two numbers{extra1}.
    The {line_order2} element contains the {op2} of the two numbers{extra2}.
    The {line_order3} element contains the {op3} of the two numbers{extra3}.
    \"\"\"
"""

def filter(vars):
    if vars['var1_name'] == vars['var2_name']: return False
    if len({vars['line_order1'], vars['line_order2'], vars['line_order3']}) < 3: return False
    if len({vars['op1'], vars['op2'], vars['op3']}) < 3: return False
    return True

GRID = {
    'var1_name': ['a', 'b', 'fkrjf4ifji4ofj'],
    'var2_name': ['a', 'b', 'fekjfwoeifjwu5gfd'],
    'line_order1': ["first", "second", "third"],
    'line_order2': ["first", "second", "third"],
    'line_order3': ["first", "second", "third"],
    'op1': ["sum", "difference", "product"],
    'op2': ["sum", "difference", "product"],
    'op3': ["sum", "difference", "product"],
}

def oracle_(input, line_order1, line_order2, line_order3, op1, op2, op3):
    line_orders = list(zip([line_order1, line_order2, line_order3], [op1, op2, op3]))
    first_op = next(o for l, o in line_orders if l == 'first')
    second_op = next(o for l, o in line_orders if l == 'second')
    third_op = next(o for l, o in line_orders if l == 'third')

    def run_op(op):
        if op == 'sum':
            return input[0] + input[1]
        elif op == 'difference':
            return input[0] - input[1]
        elif op == 'product':
            return input[0] * input[1]
        else:
            raise RuntimeError("invalid op")
        
    return (run_op(first_op), run_op(second_op), run_op(third_op))

def oracle(vars, input):
    return oracle_(input=input, **dict((k, vars[k]) for k in ('line_order1', 'line_order2', 'line_order3', 'op1', 'op2', 'op3')))

def render(**vars):
    for i in range(1, 4):
        if vars[f"op{i}"] == 'difference':
            vars[f"extra{i}"] = " (first - second)"
        else:
            vars[f"extra{i}"] = ""

    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, filter_func=filter, **kwargs)
