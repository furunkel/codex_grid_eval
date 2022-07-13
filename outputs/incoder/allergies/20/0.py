
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

    So if Alice is allergic to peanuts and pollen, he gets a score of 33.

    Now, given just that score of 33, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the peanuts (1) allergy.
    """
    
    allergies = []
    
    if score < 1:
        return allergies
    
    if score < 32:
        allergies.append('peanuts')
        return allergies
    
    if score < 64:
        allergies.append('eggs')
        return allergies
    
    if score < 128:
        allergies.append('chocolate')
        return allergies
    
    if score < 256:
        allergies.append('shellfish')
        return allergies
    
    if score < 512:
        allergies.append('cats')
        return allergies
    
    if score < 1024:
        allergies.append('pollen')
        return allergies
    
    if score < 2048:
        allergies.append('tomatoes')
        return allergies
    
    if score < 4096:
        allergies.append('strawberries')
        return allergies
    
    if score < 8192:
        allergies.append('carrots')
        return allergies
    
    if score < 16384:
        allergies.append('potatoes')
        return allergies
    
    if score < 32768:
