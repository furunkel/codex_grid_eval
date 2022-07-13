
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

    So if Alice is allergic to peanuts and shellfish, he gets a score of 6.

    Now, given just that score of 6, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergies = []
    if score < 1:
        return allergies
    if score < 2:
        allergies.append('eggs')
    if score < 4:
        allergies.append('peanuts')
    if score < 8:
        allergies.append('shellfish')
    if score < 16:
        allergies.append('strawberries')
    if score < 32:
        allergies.append('tomatoes')
    if score < 64:
        allergies.append('chocolate')
    if score < 128:
        allergies.append('pollen')
    if score < 256:
        allergies.append('cats')
    return allergies


# Problem 7
def allergies_scores(allergies):
    """
    Given a list of allergies (as returned by allergies()), return a
    dictionary mapping allergies to the score for that allergy.

    For example, given ['eggs', 'peanuts', 'shellfish'], the dictionary
    should contain {'eggs': 1, 'peanuts': 2, 'shellfish': 4}.
    """
    scores = {}
    for allergy in allergies:
        scores[allergy] = allergy_score(allergy)
    return scores


# Problem 8