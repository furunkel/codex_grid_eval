
def allergies(score):
    """
    Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * eggs (1)
    * tomatoes (2)
    * peanuts (4)
    * pollen (8)
    * strawberries (16)
    * cats (32)
    * chocolate (64)
    * shellfish (128)

    So if Destiny is allergic to peanuts and pollen, he gets a score of 12.

    Now, given just that score of 12, your program should return a list of all the allergens Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergies = []
    if score >= 1:
        allergies.append('eggs')
    if score >= 2:
        allergies.append('tomatoes')
    if score >= 4:
        allergies.append('peanuts')
    if score >= 8:
        allergies.append('pollen')
    if score >= 16:
        allergies.append('strawberries')
    if score >= 32:
        allergies.append('cats')
    if score >= 64:
        allergies.append('chocolate')
    if score >= 128:
        allergies.append('shellfish')
    return allergies


# Problem 7
def allergy_score(allergies):
    """
    Given a list of allergies (as returned by allergies()), return the
    allergy score for the person.

    For example, if the person has allergies 'eggs', 'tomatoes', and
    'peanuts', then the allergy score is 3.

    Your program should ignore the components of the allergy score
    (i.e., ignore the 'eggs' component of the allergy score).
    """
    score = 0
    for allergy in allergies:
        score += allergies[allergy