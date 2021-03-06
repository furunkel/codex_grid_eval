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

    So if Destiny is allergic to chocolate and pollen, he gets a score of 72.

    Now, given just that score of 72, your program should return a list of all the allergens Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    # TODO: implement this
    return [score] * len(score)


def get_score(person, item):
    """
    Given a person's item, return the score of the item.

    If the item is not in the list of allergies, return -1.

    If the item is in the list of allergies, return 1.

    If the item is in the list of allergies, return 0.

    If the item is in the list of allergies, return 1.

    If the item is in the list of allergies, return -1.

    If the item is in the list of allergies, return 0.

    If the item is in the list of allergies, return 1.

    If the item is in the list of allergies, return -1.

    If the item is in the list of allergies, return 0.

    If the item is in the list of allergies, return 1.

    If the item is in the list of allergies, return -1.