
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 2, 3 or 5 below 1000.
    """    
#    print multiples(2, 3, 5)
    return sum(multiples(2, 3, 5))

def multiples_with_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 2, 3 or 5 below 1000.
    """
    return sum(multiples(2, 3, 5, one_digit=True))

def multiples_with_two_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 2, 3 or 5 below 1000.
    """
    return sum(multiples(2, 3, 5, two_digit=True))

def multiples_with_three_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 2, 3 or 5 below 1000.
    """
    return sum(multiples(2, 3, 5, three_digit=True))

def multiples_with_four_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 2, 3 or 5 below 1000.
    """
    return sum(multiple