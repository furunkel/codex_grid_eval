def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 2, 3 or 5 below 500.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 15)])

def multiples_with_two_numbers():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 2, 3 or 5 below 500.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 15)])

def multiples_with_two_numbers_and_one_number():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 2, 3 or 5 below 500.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 15)])

def multiples_with_two_numbers_and_one_number_and_two_numbers():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 2, 3 or 5 below 500.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 15), y*y for y in range(1, 15)])

def multiples_with_two_numbers_and_one_number_and_two_numbers_and_two_numbers():
    """
    If