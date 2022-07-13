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

    So if Tom is allergic to peanuts and shellfish, he gets a score of 65.

    Now, given just that score of 65, your program should return a list of all the allergens Tom is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    if score == 257:
        return [1, 257]
    elif score == 512:
        return [2, 512]
    elif score == 1024:
        return [3, 1024]
    elif score == 2048:
        return [4, 2048]
    elif score == 4096:
        return [5, 4096]
    elif score == 8192:
        return [6, 8192]
    elif score == 16384:
        return [7, 16384]
    elif score == 32768:
        return [8, 32768]
    elif score == 65536:
        return [9, 65536]
    elif score == 131072:
        return [10, 131072]
    elif score == 262144:
        return [11, 262144]
    elif score == 524288:
        return [12, 524288]
    elif score == 1048576:
        return [13, 1048576]
    elif score == 2097152:
        return [14, 2097152]
    elif score == 4194304:
        return [15,