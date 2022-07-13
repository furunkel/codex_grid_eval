
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

    So if Fritz von Kitzhausdorf is allergic to peanuts and shellfish, he gets a score of 9.

    Now, given just that score of 9, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """

def allergies_from_string(string):
    """
    Given a string containing a list of allergies, return a list of all the allergies
    that were tested for.

    >>> allergies_from_string('peanuts,eggs,chocolate,cats,pollen,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,strawberries,tomatoes,straw