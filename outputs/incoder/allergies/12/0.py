
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

    So if Fritz von Kitzhausdorf is allergic to peanuts and pollen, he gets a score of 66.

    Now, given just that score of 66, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

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
        allergies.append('peanuts')
    if score < 256:
        allergies.append('shellfish')
    if score < 512:
        allergies.append('strawberries')
    if score < 1024:
        allergies.append('tomatoes')
    if score < 2048:
        allergies.append('chocolate')
    if score < 4096:
        allergies.append('pollen')
    if score < 8192:
        allergies.append('cats')
    return allergies


# Problem 8
def allergies_count(score):
    """
    Given a person's allergy score, determine whether or not they're allergic to a given item, and how many allergies they have.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * eggs (1)
    * peanuts (2)
    * shellfish (4)
    * strawberri