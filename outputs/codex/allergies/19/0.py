
def allergies(score):
    """
    Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * peanuts (1)
    * eggs (2)
    * chocolate (4)
    * shellfish (8)
    * cats (16)
    * pollen (32)
    * tomatoes (64)
    * strawberries (128)

    So if Tom is allergic to chocolate and shellfish, he gets a score of 12.

    Now, given just that score of 12, your program should return a list of all the allergens Tom is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    allergens = {
        1: 'peanuts',
        2: 'eggs',
        4: 'chocolate',
        8: 'shellfish',
        16: 'cats',
        32: 'pollen',
        64: 'tomatoes',
        128: 'strawberries'
    }

    allergies = []
    for key in sorted(allergens.keys(), reverse=True):
        if score >= key:
            allergies.append(allergens[key])
            score -= key

    return allergies