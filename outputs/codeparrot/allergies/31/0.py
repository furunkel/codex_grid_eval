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

    So if Fritz von Kitzhausdorf is allergic to chocolate and shellfish, he gets a score of 12.

    Now, given just that score of 12, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

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
    Given a person's name, return the score of that person's name.

    The score of the person's name is the number of allergens that
    person has (that they were tested for).

    The score of the person's name is the number of allergens that
    person has (that they were tested for).

    The score of the person's name is the number of allergens that
    person has (that they were tested for).

   