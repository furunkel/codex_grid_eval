def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 124.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 101) if x%2 == 0], [x*y for x in range(1, 101) if x%2 == 1], [])

def multiples_with_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 124.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 101) if x%2 == 0], [x*y for x in range(1, 101) if x%2 == 1], [])

def multiples_with_one_digit_and_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 124.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 101) if x%2 == 0], [x*y for x in range(1, 101) if x%2 == 1], [])

def multiples_with_one_digit_and_one_digit_and_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 124.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 101) if x%2 == 0], [x*y for x in