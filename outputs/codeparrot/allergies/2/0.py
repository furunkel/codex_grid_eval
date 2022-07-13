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

    So if Tom is allergic to chocolate and pollen, he gets a score of 96.

    Now, given just that score of 96, your program should return a list of all the allergens Tom is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    if score == 0:
        return [1]
    elif score == 1:
        return [2]
    elif score == 2:
        return [4]
    elif score == 4:
        return [8]
    elif score == 8:
        return [16]
    elif score == 16:
        return [32]
    else:
        return [64]


def get_score(person, item):
    """
    Given a person's item, return the score of the person's item.

    The score of the item is the number of allergens that the person has.

    The score of the item is the number of allergens that the person has.

    The score of the item is the number of allergens that the person has.

    The score of the item is the number of allergens that the person has.

    The score of the item is the number of allergens that the person has.

    The score of the item is the number of allergens that the person has.

    The score of the item is the number of allergens that the