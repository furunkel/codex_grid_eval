def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The product of these multiples is 44100.
    Return the product of all the multiples of 5, 7 or 9 below 200.
    """
    return [x for x in range(1, 101) if x % 5 == 0]

def multiples_with_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The product of these multiples is 44100.
    Return the product of all the multiples of 5, 7 or 9 below 200.
    """
    return [x for x in range(1, 101) if x % 5 == 0 and x % 7 == 0]

def multiples_with_one_digit_and_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The product of these multiples is 44100.
    Return the product of all the multiples of 5, 7 or 9 below 200.
    """
    return [x for x in range(1, 101) if x % 5 == 0 and x % 7 == 0 and x % 10 == 0]

def multiples_with_one_digit_and_one_digit_and_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The product of these multiples is 44100.
    Return the product of all the multiples of 5, 7 or 9 below 200.
    """
    return [x for x in range(1, 101) if x % 5 == 0 and x % 7 == 0 and x % 10 == 0 and x % 14 == 0]

def multiples_with_one_digit_and_one_digit_and_one_digit():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The product of these multiples is 44100.
    Return the product of all the multiples