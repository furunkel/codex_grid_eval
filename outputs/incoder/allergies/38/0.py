
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

    So if Alice is allergic to chocolate and pollen, he gets a score of 48.

    Now, given just that score of 48, your program should return a list of all the allergens Alice is allergic to.

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


# Problem 6
def allergy_score(allergies):
    """
    Given a list of allergies (as returned by allergies()), determine the
    allergic score for a person.

    For example, given ['peanuts', 'tomatoes'], return 3.

    Your program should ignore the non-allergic components of the allergies
    list.  For example, if the allergy list contains ['eggs', 'pollen'], your
    program should ignore eggs and pollen and return the allergic score for
    peanuts and tomatoes.
    """
    score = 0
    for allerg