
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The product of these multiples is 810.
    Return the product of all the multiples of 3 or 5 below 100.
    """    
#    if len(str(multiples())) == 0:
#        return 0
#    else:
#        return multiples()[0]
#
#    product = multiples()[0]
#    for i in range(1, len(multiples())):
#        product = product * multiples()[i]
#    return product

def multiples_with_one_digit(multiples):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The product of these multiples is 810.
    Return the product of all the multiples of 3 or 5 below 100.
    """
    if len(str(multiples())) == 0:
        return 0
    else:
        return multiples()[0]

def multiples_with_one_digit_and_one_digit(multiples):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The product of these multiples is 810.
    Return the product of all the multiples of 3 or 5 below 100.
    """
    if len(str(multiples())) == 0:
        return 0
    else:
        return multiples()[0] + multiples()[1] + multiples()[2]

def multiples_with_one_digit_and_one_digit_and_one_digit(multiples):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The product of these multiples is 810.
    Return the product of all the multiples of 3 or 5 below 100.
    """
    if len(str(multiples())) == 0:
        return 0
    else:
        return multiples()[0] + multiples()[1] + multiples()[2] + multiples()[3] + multiples()[4]

def multiples_with_one_digit_and_one_digit_and