
def allergies(score):
    """
    Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * peanuts (1)
    * tomatoes (2)
    * strawberries (4)
    * eggs (8)
    * pollen (16)
    * chocolate (32)
    * shellfish (64)
    * cats (128)

    So if Tom is allergic to peanuts and pollen, he gets a score of 17.

    Now, given just that score of 17, your program should return a list of all the allergens Tom is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """

def allergies_from_string(string):
    """
    Given a string, return a list of all the allergies in the string.

    >>> allergies_from_string('Mr. Mrs. Mrs.')
    ['Mr. Mrs.', 'Mrs. Mrs.', 'Mrs. Mrs.']
    """

def allergies_from_file(filename):
    """
    Given a filename, return a list of all the allergies in the file.

    >>> allergies_from_file('Mr. Mrs. Mrs.')
    ['Mr. Mrs.', 'Mrs. Mrs.', 'Mrs. Mrs.']
    """

def allergies_from_list(list):
    """
    Given a list of strings, return a list of all the allergies in the list.

    >>> allergies_from_list(['Mr. Mrs.', 'Mrs. Mrs.'])
    ['Mr. Mrs.', 'Mrs