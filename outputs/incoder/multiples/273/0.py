
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The product of these multiples is 24.
    Return the product of all the multiples of 2, 3 or 5 below 200.
    """    
    return sum([2**i for i in range(5) if i % 2 == 0 or i % 3 == 0 or i % 5 == 0])

def fibonacci():
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even-valued terms in the sequence which do not exceed four million.
    """
    return sum([i for i in range(1, 4000000) if i % 2 == 0])

def fibonacci_sum():
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even-valued terms in the sequence which do not exceed four million.
    """
    return sum([i for i in range(1, 4000000) if i % 2 == 0 and i % 3 != 0])

def fibonacci_product():
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the product of all the even-valued terms in the sequence which do not exceed four million.
    """
    return sum([i for i in range(1, 4000000) if i % 2 == 0 and i % 3 == 0])

def fibonacci_product_sum():
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the product of all the even-valued terms in the sequence which do not exceed four million.
    """
    return sum([i for i in range(1, 4000000) if i % 2 == 0 and i % 3 == 0 and i % 5 != 0])

def fibonacci_product_product():
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the product of all the even-valued terms in the sequence which do not exceed four million.
    """
    return sum([i for i in range(1, 4000000) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0])

def fibonacci_product_product_sum():
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the product of all the even-valued terms in the sequence which do not 