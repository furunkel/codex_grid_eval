
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

    So if Destiny is allergic to peanuts and shellfish, he gets a score of 65.

    Now, given just that score of 65, your program should return a list of all the allergens Destiny is allergic to.

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

# Problem 7
def allergies_count(score):
    """
    Given a person's allergy score, determine how many allergies they have.

    Your program should return a count of the number of allergies that
    Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) 