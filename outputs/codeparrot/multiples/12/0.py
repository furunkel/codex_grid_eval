
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 1000.
    """    
#    if len(str(multiples())) == 0:
#        return 0
    if len(str(multiples())) == 1:
        return int(multiples()[0])
    else:
        return int(multiples()[0]) + int(multiples()[1])

def multiples_with_one_digit(multiples):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 1000.
    """
    if len(str(multiples())) == 0:
        return 0
    if len(str(multiples())) == 1:
        return int(multiples()[0])
    else:
        return int(multiples()[0]) + int(multiples()[1])

def multiples_with_one_digit_and_one_digit(multiples):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 1000.
    """
    if len(str(multiples())) == 0:
        return 0
    if len(str(multiples())) == 1:
        return int(multiples()[0])
    else:
        return int(multiples()[0]) + int(multiples()[1]) + int(multiples()[2])

def multiples_with_one_digit_and_one_digit_and_one_digit(multiples):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 1000.
    """
    if len(str(multiples())) == 0:
        return 0
    if len(str(multiples())) == 1:
        return int(