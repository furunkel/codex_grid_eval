
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

    So if Destiny is allergic to chocolate and shellfish, he gets a score of 192.

    Now, given just that score of 192, your program should return a list of all the allergens Destiny is allergic to.

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

    result = []
    for key in sorted(allergens.keys(), reverse=True):
        if score >= key:
            result.append(allergens[key])
            score -= key
    return result


def is_allergic_to(score, item):
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

    So if Destiny is allergic to chocolate and shellfish, he gets a score of 192.

    Now, given just that score of 192, your program should return a list of all the allergens Destiny is allergic to.

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

    for key in sorted(allergens.keys(), reverse=True):
        if score >= key:
            if allergens[key] == item:
                return True
            score -=