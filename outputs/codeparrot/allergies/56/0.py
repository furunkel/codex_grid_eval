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

    So if Destiny is allergic to peanuts and pollen, he gets a score of 12.

    Now, given just that score of 12, your program should return a list of all the allergens Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    if score == 0:
        return []
    if score == 1:
        return [1]
    if score == 2:
        return [2]
    if score == 4:
        return [4]
    if score == 8:
        return [8]
    if score == 16:
        return [16]
    if score == 32:
        return [32]
    if score == 64:
        return [64]
    if score == 128:
        return [128]
    if score == 256:
        return [256]
    if score == 512:
        return [512]
    if score == 1024:
        return [1024]
    if score == 2048:
        return [2048]
    if score == 4096:
        return [4096]
    if score == 8192:
        return [8192]
    if score == 16384:
        return [16384]
    if score == 32768:
        return [32768]
    if score == 65536:
        return [65536]
    if score == 131072:
        return [131072]
    if score == 262144: