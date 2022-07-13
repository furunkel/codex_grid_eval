
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

    So if Tom is allergic to peanuts and pollen, he gets a score of 17.

    Now, given just that score of 17, your program should return a list of all the allergens Tom is allergic to.

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
        allergies.append('tomatoes')
    if score < 64:
        allergies.append('strawberries')
    if score < 128:
        allergies.append('eggs')
    if score < 256:
        allergies.append('pollen')
    if score < 512:
        allergies.append('chocolate')
    if score < 1024:
        allergies.append('shellfish')
    if score < 2048:
        allergies.append('cats')
    return allergies


def allergy_score(allergies):
    """
    Given a list of allergies, return the score that Tom would get if he
    had tested them all.  (The score is just the sum of the individual scores
    of each allergy.)

    For example, if Tom is allergic to peanuts and pollen, he would get a
    score of 17 (1 + 4 + 16 + 32 + 64 + 128 + 256).

    Your program should ignore the allergens listed above (i.e.
    allergens that score 256, 512, 1024, 