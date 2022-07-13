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

    So if Fritz von Kitzhausdorf is allergic to chocolate and pollen, he gets a score of 48.

    Now, given just that score of 48, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    # TODO: implement this
    return [
        (score, 1)
        for score in range(1, 11)
        if score % 2 == 0
    ]


def get_score_of_person(person):
    """
    Given a person's name, return the score of that person's name.

    If the person is not found, return None.

    >>> get_score_of_person('Michael')
    1
    >>> get_score_of_person('Michael')
    None
    """
    return [
        (person, 1)
        for person in Person.objects.filter(name=person)
    ]


def get_score_of_person_by_name(person_name):
    """
    Given a person's name, return the score of that person's name.

    If the person is not found, return None.

    >>> get_score_of_person_by_name('Michael')
    1
    >>> get_score_of_