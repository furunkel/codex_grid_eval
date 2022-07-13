
def allergies(score):
    """
    Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * eggs (1)
    * peanuts (2)
    * shellfish (4)
    * strawberries (8)
    * tomatoes (16)
    * chocolate (32)
    * pollen (64)
    * cats (128)

    So if Fritz von Kitzhausdorf is allergic to chocolate and pollen, he gets a score of 96.

    Now, given just that score of 96, your program should return a list of all the allergens Fritz von Kitzhausdorf is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergies = []
    if score < 0 or score > 128:
        return allergies
    
    allergies.append(1)
    allergies.append(2)
    allergies.append(4)
    allergies.append(8)
    allergies.append(16)
    allergies.append(32)
    allergies.append(64)
    allergies.append(128)
    
    return allergies

def allergies_score(allergies):
    """
    Given a list of allergies, return the score that would give each
    allergy a score of 1.

    For example, if Fritz von Kitzhausdorf has allergies of 1, 2, 4, 8, 16,
    32, 64, and 128, then his score is 96.

    Your program should return the score as a single integer.
    """
    score = 0
    for allergy in allergies:
        score += allergy
    return score

def allergies_score_with_eggs(allergies):
    """
    Given a list of allergies, return the score that would give each
    allergy a score of 1.

    For example, if Fritz von Kitzhausdorf has allergies of 1, 2, 4, 8, 16,
    32, 64, and 128, then 