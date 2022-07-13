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

    So if Tom is allergic to peanuts and shellfish, he gets a score of 9.

    Now, given just that score of 9, your program should return a list of all the allergens Tom is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    if score == 1:
        return [1]
    elif score == 2:
        return [2]
    elif score == 4:
        return [4]
    elif score == 8:
        return [8]
    elif score == 16:
        return [16]
    elif score == 32:
        return [32]
    elif score == 64:
        return [64]
    elif score == 128:
        return [128]
    else:
        return [0]


def get_score_of_person(person):
    """
    Given a person's name, return the score of that person's allergies.

    The score of the person's allergies is the number of allergies the person has.
    """
    if person == "peanuts":
        return 8
    elif person == "eggs":
        return 16
    elif person == "chocolate":
        return 32
    elif person == "shellfish":
        return 64
    elif person == "cats":
        return 128
    elif person == "pollen":
        return 256
   