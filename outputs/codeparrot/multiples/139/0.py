def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 1000.
    """
    return [n for n in range(1, 1000) if n % 3 == 0]


def multiples_with_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 1000.
    """
    return [n for n in range(1, 1000) if n % 3 == 1]


def multiples_with_one_digit_and_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 1000.
    """
    return [n for n in range(1, 1000) if n % 3 == 1 and n % 10 == 0]


def multiples_with_one_digit_and_one_digit_and_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 1000.
    """
    return [n for n in range(1, 1000) if n % 3 == 1 and n % 10 == 1]


def multiples_with_one_digit_and_one_digit_and_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 1000.
    """
    return [n for n in range(1, 1000) if n % 3 == 1 and n % 10