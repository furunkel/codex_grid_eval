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
    if score == 0:
        return [0]
    elif score == 1:
        return [1]
    elif score == 2:
        return [2]
    elif score == 3:
        return [3]
    elif score == 4:
        return [4]
    elif score == 5:
        return [5]
    elif score == 6:
        return [6]
    elif score == 7:
        return [7]
    elif score == 8:
        return [8]
    elif score == 9:
        return [9]
    elif score == 10:
        return [10]
    elif score == 11:
        return [11]
    elif score == 12:
        return [12]
    elif score == 13:
        return [13]
    elif score == 14:
        return [14]
    elif score == 15:
        return [15]
    elif score == 16:
        return [16]
    elif score == 17:
        return [17]
    elif score == 18:
        return [18]
    elif score == 19:
        return [19]
    elif score ==