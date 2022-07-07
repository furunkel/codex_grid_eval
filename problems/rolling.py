from problems.default import default_generate

TARGET = 'rolling_{op}'
INPUTS = [[[]], [[1,2,3,4]], [[4,3,2,1]], [[3,2,3,100,3]]]
TEST_IMPORTS = [('typing', ['List', 'Tuple'])]
ORIGIN = 'humaneval'

TEXT = """
def rolling_{op}(numbers: List[int]) -> List[int]:
    \"\"\" From a given list of integers, generate a list of {rolling_objective} found until given moment
    in the sequence.
    >>> rolling_{op}({example_input})
    {example_output}
    \"\"\"
"""

ROLLING_OBJECTIVE = {
    'min': "rolling minimum element",
    'max': "rolling maximum element",
    'sum': "rolling sum",
}

GRID = {
    'op': ['min', 'max', 'sum'],
    'example_input': [[1, 2, 3, 2, 3, 4, 2],
                      [1, 2, 2, 2],
                      [434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489]],
}

def oracle_(input, op):
    running = None
    result = []

    if input == []: return input

    for n in input:
        if running is None:
            running = n
        else:
            if op == 'max':
                running = max(running, n)
            elif op == 'min':
                running = min(running, n)
            elif op == 'sum':
                running = running + n

        result.append(running)

    return result

def oracle(vars):
    return oracle_(input=vars['input'][0], op=vars['op'])

def render(**vars):
    vars['rolling_objective'] = ROLLING_OBJECTIVE[vars['op']]
    vars['example_output'] = oracle_(input=vars['example_input'], op=vars['op'])
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, **kwargs)
