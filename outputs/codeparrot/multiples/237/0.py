
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 3 or 5, we get  and 3. The product of these multiples is 3.
    Return the product of all the multiples of 3 or 5 below 1000.
    """    
#    print multiples()
    product = 1
    for i in range(1, 1000):
        product *= multiples()
    return product

def multiples_with_one_digit():
    """
    If we list all the natural numbers below 1000 that are multiples of 3 or 5, we get  and 3. The product of these multiples is 3.
    Return the product of all the multiples of 3 or 5 below 1000.
    """
    product = 1
    for i in range(1, 1000):
        product *= multiples_with_one_digit()
    return product

def multiples_with_two_digit():
    """
    If we list all the natural numbers below 1000 that are multiples of 3 or 5, we get  and 3. The product of these multiples is 3.
    Return the product of all the multiples of 3 or 5 below 1000.
    """
    product = 1
    for i in range(1, 1000):
        product *= multiples_with_two_digit()
    return product

def multiples_with_three_digit():
    """
    If we list all the natural numbers below 1000 that are multiples of 3 or 5, we get  and 3. The product of these multiples is 3.
    Return the product of all the multiples of 3 or 5 below 1000.
    """
    product = 1
    for i in range(1, 1000):
        product *= multiples_with_three_digit()
    return product

def multiples_with_four_digit():
    """
    If we list all the natural numbers below 1000 that are multiples of 3 or 5, we get  and 3. The product of these multiples is 3.
    Return the product of all the multiples of 3 or 5 below 1000.
    """
    product = 1
    for i in range(1, 1000):
        product *= multiples_with_four_digit()
    return product

def multiples_with_five_digit():
    """
    If we list all the natural numbers below 1000 that are multiples of 3 or 5, we get  and 3. The product of