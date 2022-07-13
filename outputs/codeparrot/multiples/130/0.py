
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 5 or 3 below 197.
    """    
#    if len(str(multiples())) == 1:
#        return 3
#    else:
#        return sum(multiples())

def multiples_with_one_digit(multiples):
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 5 or 3 below 197.
    """
    if len(str(multiples())) == 1:
        return 3
    else:
        return sum(multiples_with_one_digit(multiples))

def multiples_with_one_digit_with_one_digit(multiples):
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 5 or 3 below 197.
    """
    if len(str(multiples())) == 1:
        return 3
    else:
        return sum(multiples_with_one_digit_with_one_digit(multiples))

def multiples_with_one_digit_with_one_digit_with_one_digit(multiples):
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 5 or 3 below 197.
    """
    if len(str(multiples())) == 1:
        return 3
    else:
        return sum(multiples_with_one_digit_with_one_digit_with_one_digit(multiples))

def multiples_with_one_digit_with_one_digit_with_one_digit(multiples):
    """
    If we list all the natural numbers below