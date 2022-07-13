
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

    So if Alice is allergic to chocolate and shellfish, he gets a score of 96.

    Now, given just that score of 96, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    score = int(score)
    allergies = []
    if score >= 0 and score <= 1:
        allergies.append('peanuts')
    if score >= 2 and score <= 4:
        allergies.append('tomatoes')
    if score >= 8 and score <= 16:
        allergies.append('eggs')
    if score >= 32 and score <= 64:
        allergies.append('pollen')
    if score >= 128 and score <= 256:
        allergies.append('chocolate')
    if score >= 256 and score <= 512:
        allergies.append('shellfish')
    if score >= 512 and score <= 1024:
        allergies.append('cats')
    return allergies


def allergy_score(allergies):
    """
    Given a list of allergies (as returned by `allergies()`), return the
    allergy score for the person.

    For example, if `allergies` contains 'peanuts', the score is 1.
    If `allergies` contains 'eggs', the score is 8.
    """
    score = 0
    for allergy in allergies:
        if allergy == 'peanuts':
            score += 1
        if allergy == 'eggs':
