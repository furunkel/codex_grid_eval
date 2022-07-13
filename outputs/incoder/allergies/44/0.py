
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

    So if Fritz von Kitzhausdorf is allergic to peanuts and pollen, he gets a score of 17.

    Now, given just that score of 17, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    allergies = []
    score = int(score)
    if score < 1:
        return allergies
    if score < 32:
        allergies.append('peanuts')
    if score < 64:
        allergies.append('tomatoes')
    if score < 128:
        allergies.append('strawberries')
    if score < 256:
        allergies.append('eggs')
    if score < 512:
        allergies.append('pollen')
    if score < 1024:
        allergies.append('chocolate')
    if score < 2048:
        allergies.append('shellfish')
    if score < 4096:
        allergies.append('cats')
    return allergies


# Problem #6
def allergy_score(allergies):
    """
    Given a list of allergies, return the score for a person who is allergic to all of them.

    For example, if the person is allergic to peanuts and strawberries, their score is 17.  If the person is allergic to eggs, their score is 19.  If the person is allergic to all of them, their score is 0.
    """
    score = 0
    for allergy in allergies:
        score 