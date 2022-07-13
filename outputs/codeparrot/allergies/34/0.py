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

    So if Tom is allergic to chocolate and pollen, he gets a score of 48.

    Now, given just that score of 48, your program should return a list of all the allergens Tom is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    if score == 0:
        return [1]
    elif score == 1:
        return [2]
    elif score == 2:
        return [3]
    elif score == 3:
        return [4]
    elif score == 4:
        return [5]
    elif score == 5:
        return [6]
    elif score == 6:
        return [7]
    elif score == 7:
        return [8]
    elif score == 8:
        return [9]
    elif score == 9:
        return [10]
    elif score == 10:
        return [11]
    else:
        return [12]


def get_score_of_person(person):
    """
    Given a person's name, return the score of that person.

    If the person is not found, return None.
    """
    if person in person_list:
        return person_list.index(person)
    else:
        return None


def get_score_of_item(item):
    """
    Given a item's name, return the score of that item.