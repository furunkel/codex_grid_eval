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

    So if Destiny is allergic to peanuts and shellfish, he gets a score of 9.

    Now, given just that score of 9, your program should return a list of all the allergens Destiny is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    if score == 0:
        return []
    if score == 1:
        return [1]
    if score == 2:
        return [2]
    if score == 3:
        return [3]
    if score == 4:
        return [4]
    if score == 5:
        return [5]
    if score == 6:
        return [6]
    if score == 7:
        return [7]
    if score == 8:
        return [8]
    if score == 9:
        return [9]
    if score == 10:
        return [10]
    if score == 11:
        return [11]
    if score == 12:
        return [12]
    if score == 13:
        return [13]
    if score == 14:
        return [14]
    if score == 15:
        return [15]
    if score == 16:
        return [16]
    if score == 17:
        return [17]
    if score == 18:
        return [18]
    if score == 19:
        return [19]
    if