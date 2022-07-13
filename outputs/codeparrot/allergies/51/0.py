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

    So if Tom is allergic to chocolate and shellfish, he gets a score of 192.

    Now, given just that score of 192, your program should return a list of all the allergens Tom is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    if score < 192:
        return [1, 257]
    elif score < 512:
        return [2, 512]
    elif score < 1024:
        return [4, 1024]
    elif score < 2048:
        return [8, 2048]
    else:
        return [16, 2048]


def get_score(person, item):
    """
    Given a person's item, return the score of that person's item.

    The score is the number of items that the person has.  If the item is
    a string, then it is assumed to be a number.  If the item is a list, then
    it is assumed to be a list of strings.  If the item is a tuple, then
    it is assumed to be a tuple of strings.  If the item is a string, then
    it is assumed to be a string.  If the item is a list, then it is assumed to be a
    list of strings.  If the item is a tuple, then it is assumed to be a
    tuple of strings.  If the