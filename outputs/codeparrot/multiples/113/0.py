def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 100.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 101) if x%2 == 0])


def multiples_with_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 100.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 101) if x%2 == 0 and x%3 == 0])


def multiples_with_two_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 100.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 101) if x%2 == 0 and x%3 == 0 and x%5 == 0])


def multiples_with_three_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 100.
    """
    return reduce(lambda x, y: x*y, [x*y for x in range(1, 101) if x%2 == 0 and x%3 == 0 and x%5 == 0])


def multiples_with_four_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
   