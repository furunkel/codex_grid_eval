from collections import defaultdict
from problems.default import default_generate
import re

TYPE_NAMES = {
    'tlh': {
        'integer': 'ngeb',
        'tuple': 'cheng',
        'dictionary': "mu_ghom",
        'list': 'telth',
        'float': 'tlhim',
        'string': 'SIrgh'
    }
}

TARGET = {'': 'filter_{type}s', 'tlh': lambda l, v: f'chol_{TYPE_NAMES[l][v["type"]]}'}
INPUTS = [[[4, {}, [], 23.2, 9, 'adasd']], [[3, 'c', 3, 3, 'a', 'b']]] 
TEST_IMPORTS = [('typing', ['List', 'Any', 'Dict', 'Tuple'])]

TEXT = """
def filter_{type}s(values: List[Any]) -> List[{decl_type}]:
    \"\"\" Filter given list of any python values only for {type}s
    >>> filter_{type}s({example_input})
    {example_output}
    \"\"\"
"""

TEXT_TLH = """
def chol_{type_name}(values: List[Any]) -> List[{decl_type}]:
    \"\"\" yapbe'mo' yoHwI'pu' {type_name}
    >>> chol_{type_name}({example_input})
    {example_output}
    \"\"\"
"""

TEXTS = {
    'tlh': TEXT_TLH,
    '': TEXT
}

DECL_TYPE = {
    'string': 'str',
    'integer': 'int',
    'tuple': 'Tuple',
    'dictionary': 'Dict[Any, Any]',
    'list': 'List[Any]',
    'float': 'float',
}

PYTHON_TYPE = {
    'string': str,
    'integer': int,
    'tuple': tuple,
    'dictionary': dict,
    'list': list,
    'float': float,
}

GRID = {
    'type': ['string', 'integer', 'float', 'dictionary', 'list', 'tuple'],
    'example_input': [['a', 3.14, 5], [1, 2, 3, 3.6, 'abc', {}, [], (1,)]]
}

def oracle_(input, type):
    return [x for x in input if isinstance(x, PYTHON_TYPE[type])]

def oracle(vars):
    return oracle_(input=vars['input'][0], type=vars['type'])

def render(lang, **vars):
    vars['decl_type'] = DECL_TYPE[vars['type']]
    if lang in TYPE_NAMES:
        vars['type_name'] = TYPE_NAMES[lang][vars['type']]
    vars['example_output'] = oracle_(input=vars['example_input'], type=vars['type'])
    return TEXTS[lang].format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, **kwargs)
