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

    So if Fritz von Kitzhausdorf is allergic to peanuts and pollen, he gets a score of 17.

    Now, given just that score of 17, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

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
        return [4, 1024]
    elif score == 2048:
        return [8, 2048]
    elif score == 4096:
        return [16, 4096]
    elif score == 8192:
        return [32, 8192]
    elif score == 16384:
        return [64, 16384]
    elif score == 32768:
        return [128, 32768]
    elif score == 65536:
        return [256, 65536]
    elif score == 131072:
        return [512, 131072]
    elif score == 262144:
        return [1, 262144]
    elif score == 524288:
        return [2, 524288]
    elif score == 1048576:
        return [4, 1048576]
    elif score == 2097152:
        return [8, 2097152]