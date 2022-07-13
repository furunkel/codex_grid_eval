
def allergies(score):
    """
    Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * eggs (1)
    * tomatoes (2)
    * peanuts (4)
    * pollen (8)
    * strawberries (16)
    * cats (32)
    * chocolate (64)
    * shellfish (128)

    So if Fritz von Kitzhausdorf is allergic to peanuts and pollen, he gets a score of 12.

    Now, given just that score of 12, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """

def allergies_from_string(string):
    """
    Given a string, return a list of allergies.

    >>> allergies_from_string('eggs')
    ['eggs']
    >>> allergies_from_string('tomatoes')
    ['tomatoes']
    >>> allergies_from_string('peanuts')
    ['peanuts']
    >>> allergies_from_string('pollen')
    ['pollen']
    >>> allergies_from_string('strawberries')
    ['strawberries']
    >>> allergies_from_string('chocolate')
    ['chocolate']
    >>> allergies_from_string('shellfish')
    ['shellfish']
    >>> allergies_from_string('cats')
    ['cats']
    >>> allergies_from_string('chocolate')
    ['chocolate']
    >>> allergies