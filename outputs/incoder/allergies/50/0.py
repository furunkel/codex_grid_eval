
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

    So if Tom is allergic to chocolate and pollen, he gets a score of 72.

    Now, given just that score of 72, your program should return a list of all the allergens Tom is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergies = []
    if score < 0 or score > 128:
        return allergies
    
    allergies.append('eggs')
    allergies.append('tomatoes')
    allergies.append('peanuts')
    allergies.append('pollen')
    allergies.append('strawberries')
    allergies.append('cats')
    allergies.append('chocolate')
    allergies.append('shellfish')
    
    return allergies

def allergies_score(allergies):
    """
    Given a list of allergies (as returned from allergies()), determine the
    score for that list of allergies.

    A score of 0 means no allergies were tested, and a score of 128 means
    all allergies were tested.

    For example, given allergies = ['eggs', 'tomatoes', 'peanuts', 'pollen',
    'strawberries', 'cats', 'chocolate', 'shellfish'], your program should
    return 72.
    """
    score = 0
    for allergy in allergies:
        score += allergies[allergy]
    return score

def allergies_score_to_list(aller