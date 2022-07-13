
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

    So if Destiny is allergic to peanuts and pollen, he gets a score of 33.

    Now, given just that score of 33, your program should return a list of all the allergens Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    allergies = []
    if score < 1:
        return allergies
    if score < 2:
        allergies.append('peanuts')
        return allergies
    if score < 4:
        allergies.append('eggs')
        return allergies
    if score < 8:
        allergies.append('chocolate')
        return allergies
    if score < 16:
        allergies.append('shellfish')
        return allergies
    if score < 32:
        allergies.append('cats')
        return allergies
    if score < 64:
        allergies.append('pollen')
        return allergies
    if score < 128:
        allergies.append('tomatoes')
        return allergies
    if score < 256:
        allergies.append('strawberries')
        return allergies
    return allergies

# Problem #6
def allergy_score(allergies):
    """
    Given a list of allergens tested by the allergies function, determine the
    allergic score of the person who tested them.

    For example, if Destiny is allergic to peanuts and pollen, his allergic score
    is 33 (peanuts and pollen have 33