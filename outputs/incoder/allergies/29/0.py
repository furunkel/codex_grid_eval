
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
    allergies = []
    if score < 1:
        return allergies
    elif score < 4:
        allergies.append('peanuts')
    elif score < 8:
        allergies.append('eggs')
    elif score < 16:
        allergies.append('chocolate')
    elif score < 32:
        allergies.append('shellfish')
    elif score < 64:
        allergies.append('cats')
    elif score < 128:
        allergies.append('pollen')
    elif score < 256:
        allergies.append('tomatoes')
    elif score < 512:
        allergies.append('strawberries')
    else:
        allergies.append('none')
    return allergies


# Problem #6
def allergies_score(allergies):
    """
    Given a list of allergies (as returned by `allergies()`), return the
    allergy score for a person who has them allergic to all of them.

    For example, if the person has the following allergies:

    * peanuts (1)
    * eggs (2)
    * chocolate (4)
    * shellfish (8)
    * cats (16)
    * pollen (32)
    * tomatoes (