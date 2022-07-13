
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

    So if Alice is allergic to peanuts and pollen, he gets a score of 17.

    Now, given just that score of 17, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    allergies = []
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


# Problem 7
def allergies_score(allergies):
    """
    Given a list of allergies (as returned by allergies), return the
    allergy score for the person.

    For example, if Alice has allergies 'peanuts', 'tomatoes', and
    'strawberries', then his allergy score is 17.

    Your program should ignore the allergens that are not listed above
    (e.g., eggs, chocolate, etc.).
    """
    score = 0
    for allergy in 