
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

    So if Tom is allergic to peanuts and pollen, he gets a score of 66.

    Now, given just that score of 66, your program should return a list of all the allergens Tom is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergies = []
    if score < 0 or score > 128:
        return allergies
    
    allergies.append(eggs(score))
    allergies.append(peanuts(score))
    allergies.append(shellfish(score))
    allergies.append(strawberries(score))
    allergies.append(tomatoes(score))
    allergies.append(chocolate(score))
    allergies.append(pollen(score))
    allergies.append(cats(score))
    
    return allergies

def allergies_score(allergies):
    """
    Given a list of allergies, return the score that Tom would receive if he was allergic to all the allergies.

    For example, if Tom is allergic to eggs, peanuts, and pollen, his allergy score would be 66.

    Your program should return this score as a single integer.
    """
    score = 0
    for allergy in allergies:
        score += allergy
    
    return score

def allergies_scores(allergies):
    """
    Given a list of allergies, return the scores that Tom would receive if he was allergic to all the allergies.