
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

    So if Alice is allergic to peanuts and shellfish, he gets a score of 65.

    Now, given just that score of 65, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    allergies = []
    score = int(score)
    if score < 0 or score > 128:
        return allergies
    if score >= 64:
        allergies.append('peanuts')
    if score >= 32:
        allergies.append('tomatoes')
    if score >= 16:
        allergies.append('strawberries')
    if score >= 8:
        allergies.append('eggs')
    if score >= 4:
        allergies.append('pollen')
    if score >= 2:
        allergies.append('chocolate')
    if score >= 1:
        allergies.append('shellfish')
    if score >= 1:
        allergies.append('cats')
    return allergies


def allergies_count(score):
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