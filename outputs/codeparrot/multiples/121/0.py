
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 500.
    """    
#    if len(str(multiples())) == 0:
#        return 0
    if len(str(multiples())) == 1:
        return multiples()[0]
    else:
        return multiples()[0] + multiples()[1]

def multiples_with_one_digit(multiples):
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 500.
    """
    if len(str(multiples())) == 0:
        return 0
    if len(str(multiples())) == 1:
        return multiples()[0]
    else:
        return multiples()[0] + multiples()[1] + multiples()[2]

def multiples_with_one_digit_and_one_digit(multiples):
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 500.
    """
    if len(str(multiples())) == 0:
        return 0
    if len(str(multiples())) == 1:
        return multiples()[0]
    else:
        return multiples()[0] + multiples()[1] + multiples()[2] + multiples()[3]

def multiples_with_one_digit_and_one_digit_and_one_digit(multiples):
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 500.
    """
    if len(str(multiples())) == 0:
        return 0
    if len(