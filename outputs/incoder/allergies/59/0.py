
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

    So if Destiny is allergic to chocolate and shellfish, he gets a score of 192.

    Now, given just that score of 192, your program should return a list of all the allergens Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergies = []
    if score >= 64:
        allergies.append('eggs')
    if score >= 128:
        allergies.append('chocolate')
    if score >= 256:
        allergies.append('shellfish')
    if score >= 512:
        allergies.append('peanuts')
    if score >= 1024:
        allergies.append('tomatoes')
    if score >= 2048:
        allergies.append('pollen')
    if score >= 4096:
        allergies.append('strawberries')
    if score >= 8192:
        allergies.append('cats')
    return allergies


# Problem 7
def allergies_score(allergies):
    """
    Given a list of allergies (as returned by allergies()), return the
    allergy score for that list of allergies.

    For example, if allergies is ['eggs', 'chocolate', 'shellfish'], then
    allergies_score() should return 192 -- that is, Destiny is allergic to all
    three of the allergies (and no others).

    If you have no allergies, return 0.
    """
    score = 0
    for allergy in allerg