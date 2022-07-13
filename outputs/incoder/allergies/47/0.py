
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

    So if Fritz von Kitzhausdorf is allergic to chocolate and shellfish, he gets a score of 96.

    Now, given just that score of 96, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    allergies = []
    allergies.append(1)
    allergies.append(2)
    allergies.append(4)
    allergies.append(8)
    allergies.append(16)
    allergies.append(32)
    allergies.append(64)
    allergies.append(128)

    allergy_score = 0
    if score >= 1 and score <= 4:
        allergy_score += score
    if score >= 5 and score <= 8:
        allergy_score += score
    if score >= 9 and score <= 16:
        allergy_score += score
    if score >= 17 and score <= 32:
        allergy_score += score
    if score >= 33 and score <= 64:
        allergy_score += score
    if score >= 65 and score <= 128:
        allergy_score += score

    return allergies

# Problem #6
def allergy_score(allergies):
    """
    Given a list of allergies (as returned by the allergies function), calculate
    and return the allergy score for the person who has just been hired.

    Allergies are scored as follows:

    * peanuts (1)
    * tomatoes (2)
    * strawberries (4)