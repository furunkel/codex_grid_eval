def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 600.
    """
    return [n for n in range(1, 6) if n % 3 == 0]


def multiples_with_duplicates():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 600.
    """
    return [n for n in range(1, 6) if n % 3 == 0 and n % 5 == 0]


def multiples_with_duplicates_and_duplicates():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 600.
    """
    return [n for n in range(1, 6) if n % 3 == 0 and n % 5 == 0 and n % 7 == 0]


def multiples_with_duplicates_and_duplicates_and_duplicates():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 600.
    """
    return [n for n in range(1, 6) if n % 3 == 0 and n % 5 == 0 and n % 7 == 0 and n % 9 == 0]


def multiples_with_duplicates_and_duplicates_and_duplicates():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 5 or 3 below 600.
    """
    return [n for n in range(1, 6) if n % 3