
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

    So if Alice is allergic to peanuts and pollen, he gets a score of 66.

    Now, given just that score of 66, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergies = []
    if score >= 1:
        allergies.append('eggs')
    if score >= 2:
        allergies.append('peanuts')
    if score >= 4:
        allergies.append('shellfish')
    if score >= 8:
        allergies.append('strawberries')
    if score >= 16:
        allergies.append('tomatoes')
    if score >= 32:
        allergies.append('chocolate')
    if score >= 64:
        allergies.append('pollen')
    if score >= 128:
        allergies.append('cats')
    return allergies

# Problem #7
def allergy_score(allergies):
    """
    Given a list of allergies (as returned by allergies()), return the
    allergy score for a person who has allergic to *all* the allergies
    in the list.

    For example, given ['eggs', 'peanuts', 'pollen'], return 66.

    Since the list of allergies is not necessarily exhaustive, your program
    should continue to test the list of allergies until it finds an allergy
    that scores higher than the given score.

    For example, given ['eggs', 'pe