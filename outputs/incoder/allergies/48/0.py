
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

    So if Tom is allergic to peanuts and pollen, he gets a score of 12.

    Now, given just that score of 12, your program should return a list of all the allergens Tom is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergies = []
    if score < 1:
        return allergies
    if score < 64:
        allergies.append('eggs')
    if score < 128:
        allergies.append('tomatoes')
    if score < 256:
        allergies.append('peanuts')
    if score < 512:
        allergies.append('pollen')
    if score < 1024:
        allergies.append('strawberries')
    if score < 2048:
        allergies.append('cats')
    if score < 4096:
        allergies.append('chocolate')
    if score < 8192:
        allergies.append('shellfish')
    return allergies


# Problem 8
def allergies_score(allergies):
    """
    Given a list of allergies, return the score that Tom would get if he
    had tested them all.  (The score is just the sum of all the allergies
    scores Tom would get if he had tested them all.)

    For example, if Tom had tested the eggs, tomatoes, and peanuts allergies,
    then the score would be 3.

    Your program should return the score as a single integer.
    """
    score = 0
