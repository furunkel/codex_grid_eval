
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

    So if Destiny is allergic to chocolate and pollen, he gets a score of 48.

    Now, given just that score of 48, your program should return a list of all the allergens Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    allergies = []
    if score >= 1:
        allergies.append('peanuts')
    if score >= 2:
        allergies.append('tomatoes')
    if score >= 4:
        allergies.append('strawberries')
    if score >= 8:
        allergies.append('eggs')
    if score >= 16:
        allergies.append('pollen')
    if score >= 32:
        allergies.append('chocolate')
    if score >= 64:
        allergies.append('shellfish')
    if score >= 128:
        allergies.append('cats')
    return allergies


# Problem 4
def allergies_score(allergies):
    """
    Given a list of allergies (as returned by allergies()), determine the
    score for that list of allergies.

    For example, given ['peanuts', 'tomatoes', 'strawberries'], the
    allergy score is 4.

    Your program should return a score of 4.
    """
    score = 0
    for allergy in allergies:
        score += allergies[allergy]
    return score


# Problem 5
def allergies_score_2(allergies):
    """
    Given 