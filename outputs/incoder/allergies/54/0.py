
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

    So if Alice is allergic to chocolate and pollen, he gets a score of 72.

    Now, given just that score of 72, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergies = []
    if score < 1:
        return allergies
    
    score = score % 64
    if score < 32:
        allergies.append('eggs')
    if score < 64:
        allergies.append('tomatoes')
    if score < 96:
        allergies.append('peanuts')
    if score < 128:
        allergies.append('pollen')
    if score < 160:
        allergies.append('strawberries')
    if score < 192:
        allergies.append('cats')
    if score < 224:
        allergies.append('chocolate')
    if score < 256:
        allergies.append('shellfish')
    return allergies

def allergies_count(score):
    """
    Given a person's allergy score, determine how many allergies the person has (that they were tested).

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * eggs (1)
    * tomatoes (2)
    * peanuts (4)
    * pollen