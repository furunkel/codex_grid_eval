
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

    So if Fritz von Kitzhausdorf is allergic to peanuts and pollen, he gets a score of 33.

    Now, given just that score of 33, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    allergies = []
    if score < 1:
        return allergies
    elif score < 16:
        allergies.append('peanuts')
    elif score < 32:
        allergies.append('eggs')
    elif score < 64:
        allergies.append('chocolate')
    elif score < 128:
        allergies.append('shellfish')
    elif score < 256:
        allergies.append('cats')
    elif score < 512:
        allergies.append('pollen')
    elif score < 1024:
        allergies.append('tomatoes')
    elif score < 2048:
        allergies.append('strawberries')
    else:
        allergies.append('none')
    return allergies


def allergy_score(allergies):
    """
    Given a list of allergies (as returned by `allergies()`), return the
    score that should be given to each allergy.

    For example, given `allergies(['peanuts', 'pollen'])`, this function
    should return `[16, 32]`.

    Your program should ignore the allergens listed above (i.e.
    allergens that score 256, 512, 1024, etc.).
    """
    score = 0
    for 