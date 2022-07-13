
def allergies(score):
    """
    Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * eggs (1)
    * peanuts (2)
    * shellfish (4)
    * strawberries (8)
    * tomatoes (16)
    * chocolate (32)
    * pollen (64)
    * cats (128)

    So if Destiny is allergic to peanuts and pollen, he gets a score of 66.

    Now, given just that score of 66, your program should return a list of all the allergens Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergies = []
    if score < 1:
        return allergies
    elif score < 32:
        allergies.append('eggs')
    elif score < 64:
        allergies.append('peanuts')
    elif score < 128:
        allergies.append('shellfish')
    elif score < 256:
        allergies.append('strawberries')
    elif score < 512:
        allergies.append('tomatoes')
    elif score < 1024:
        allergies.append('chocolate')
    elif score < 2048:
        allergies.append('pollen')
    elif score < 4096:
        allergies.append('cats')
    else:
        allergies.append('other')
    return allergies


def allergies_score(allergies):
    """
    Given a list of allergies, return the score for that list of allergies.

    For example, if allergies is ['eggs', 'peanuts', 'pollen'], then this
    function should return 66.
    """
    score = 0
    for allergy in allergies:
        score += allergy_values[allergy]
    return score


def allergies_score_string(allergies):
    """
    Given a list of allergies, 