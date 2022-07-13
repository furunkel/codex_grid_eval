
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

    So if Destiny is allergic to chocolate and pollen, he gets a score of 36.

    Now, given just that score of 36, your program should return a list of all the allergens Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    allergies = []
    if score < 1:
        return allergies
    if score < 16:
        allergies.append('peanuts')
    if score < 32:
        allergies.append('eggs')
    if score < 64:
        allergies.append('chocolate')
    if score < 128:
        allergies.append('shellfish')
    if score < 256:
        allergies.append('cats')
    if score < 512:
        allergies.append('pollen')
    if score < 1024:
        allergies.append('tomatoes')
    if score < 2048:
        allergies.append('strawberries')
    return allergies


def allergy_score(allergies):
    """
    Given a list of allergies (strings), return the score that Destiny would get if they were all allergic to them.

    For example, if Destiny had a score of 36, and they had allergies of 'peanuts', 'eggs', 'chocolate', and 'pollen', the function should return 256.

    Your program should ignore allergens that are not listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.