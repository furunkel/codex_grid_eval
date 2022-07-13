
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

    So if Fritz von Kitzhausdorf is allergic to chocolate and shellfish, he gets a score of 192.

    Now, given just that score of 192, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

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

# Problem 3
def allergies_score(allergies):
    """
    Given a list of allergies, return the score that would be
    produced if all were tested.

    For example, if Fritz von Kitzhausdorf had the following
    allergies: eggs, tomatoes, peanuts, pollen, strawberries, cats,
    chocolate, shellfish, then his score would be 192 because he would
    have tested for all the allergies listed above.

    