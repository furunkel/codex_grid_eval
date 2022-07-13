
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

    So if Destiny is allergic to chocolate and shellfish, he gets a score of 12.

    Now, given just that score of 12, your program should return a list of all the allergens Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    allergies = []
    if score < 1:
        return allergies
    if score < 4:
        allergies.append('peanuts')
    if score < 8:
        allergies.append('eggs')
    if score < 16:
        allergies.append('chocolate')
    if score < 32:
        allergies.append('shellfish')
    if score < 64:
        allergies.append('cats')
    if score < 128:
        allergies.append('pollen')
    if score < 256:
        allergies.append('tomatoes')
    if score < 512:
        allergies.append('strawberries')
    return allergies


def allergies_score(allergies):
    """
    Given a list of allergies (as returned by allergies()), return the
    allergy score for the person.

    For example, if Destiny is allergic to peanuts and chocolate, then
    your program should return 257.
    """
    score = 0
    for allergy in allergies:
        score += allergies[allergy]
    return score


def allergies_list(allergies):
    """
    Given a list of allergies (as returned by aller