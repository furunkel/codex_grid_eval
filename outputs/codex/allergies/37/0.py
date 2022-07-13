
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

    So if Alice is allergic to peanuts and shellfish, he gets a score of 132.

    Now, given just that score of 132, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergens = {
        1: 'eggs',
        2: 'tomatoes',
        4: 'peanuts',
        8: 'pollen',
        16: 'strawberries',
        32: 'cats',
        64: 'chocolate',
        128: 'shellfish'
    }

    allergies = []
    for key in sorted(allergens.keys(), reverse=True):
        if score >= key:
            allergies.append(allergens[key])
            score -= key

    return allergies