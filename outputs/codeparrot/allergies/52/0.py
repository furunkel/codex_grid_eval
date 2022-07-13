
def allergies(score):
    """
    Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * peanuts (1)
    * eggs (2)
    * chocolate (4)
    * shellfish (8)
    * cats (16)
    * pollen (32)
    * tomatoes (64)
    * strawberries (128)

    So if Alice is allergic to peanuts and pollen, he gets a score of 33.

    Now, given just that score of 33, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """

def allergies_from_string(string):
    """
    Given a string, return a list of all the allergies of that string.

    >>> allergies_from_string('peanuts')
    ['peanuts']
    >>> allergies_from_string('eggs')
    ['eggs']
    >>> allergies_from_string('chocolate')
    ['chocolate']
    >>> allergies_from_string('shellfish')
    ['shellfish']
    >>> allergies_from_string('cats')
    ['cats']
    >>> allergies_from_string('pollen')
    ['pollen']
    >>> allergies_from_string('tomatoes')
    ['tomatoes']
    >>> allergies_from_string('strawberries')
    ['strawberries']
    >>> allergies_from_string('tomatoes', 'strawberries')
    ['tomatoes', 'st