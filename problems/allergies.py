from problems.default import default_generate
from itertools import permutations, islice
import random

ALLERGENS = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
INPUTS = list(range(1, 128))
TARGET = "allergies"
ORIGIN = "exercism"


def bullet_list(allergens):
    return "\n".join([f"    * {a} ({1 << i})" for i, a in enumerate(allergens)])

TEXT = """
def allergies(score):
    \"\"\"
    Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

{bullet_list}

    So if {name} is allergic to {example_allergen1} and {example_allergen2}, he gets a score of {example_score}.

    Now, given just that score of {example_score}, your program should return a list of all the allergens {name} is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the {allergen1} (1) allergy.
    \"\"\"
"""

def allergen_permutations(n):
    perms = set()
    random.seed(42)
    while len(perms) < n - 1:
        perms.add(tuple(random.sample(ALLERGENS, k=len(ALLERGENS))))

    return [ALLERGENS, *perms]

def filter(vars):
    if vars['example_allergen1'] == vars['example_allergen2']: return False
    return True

GRID = {
    'all_allergens': allergen_permutations(4),
    'name': ['Tom', 'Alice', 'Destiny', 'Fritz von Kitzhausdorf'],
    'example_allergen1': ['peanuts', 'chocolate'],
    'example_allergen2': ['pollen', 'shellfish'],
}

def is_output_equal(a, b):
    # disregard order
    if a is None or b is None: return False
    return set(a) == set(b)

def calc_score(all_alergens, allergens):
    return sum([(1 << all_alergens.index(a)) for a in allergens])

def oracle_(all_allergens, score):
    allergens = []
    for i, a in enumerate(all_allergens):
        if score & (1 << i):
            allergens.append(a)

    return allergens

def oracle(vars, input):
    return oracle_(vars['all_allergens'], input)

def render(**vars):

    all_allergens = vars['all_allergens']
    vars['bullet_list'] = bullet_list(all_allergens)
    vars['example_score'] = calc_score(all_allergens, [vars['example_allergen1'], vars['example_allergen2']])
    vars['allergen1'] = all_allergens[0]

    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, filter_func=filter, **kwargs)
