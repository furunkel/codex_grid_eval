
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

    So if Alice is allergic to chocolate and shellfish, he gets a score of 36.

    Now, given just that score of 36, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    score = int(score)
    allergies = []
    if score < 1:
        return allergies
    if score < 32:
        allergies.append('eggs')
    if score < 64:
        allergies.append('peanuts')
    if score < 128:
        allergies.append('shellfish')
    if score < 256:
        allergies.append('strawberries')
    if score < 512:
        allergies.append('tomatoes')
    if score < 1024:
        allergies.append('chocolate')
    if score < 2048:
        allergies.append('pollen')
    if score < 4096:
        allergies.append('cats')
    return allergies


def allergy_score(allergies):
    """
    Given a list of allergies (as returned by `allergies()`), return the
    allergy score for a person with those allergies.

    For example, if `allergies` contains 'eggs', 'peanuts', and 'chocolate',
    then `allergy_score('eggs, peanuts, chocolate')` should return 256.

    Your program should ignore the allergens listed above (i.e.
    allergen