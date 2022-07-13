
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5 or 3, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 5 or 3 below 1000.
    """    
    sum = 0
    for i in range(1, 1000):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum

# Problem 5
def fibonacci():
    """
    By listing the first six numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    sum = 0
    a, b = 0, 1
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 6
def fibonacci_sum():
    """
    By listing the first six numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    sum = 0
    a, b = 0, 1
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 7
def fibonacci_sum_of_squares():
    """
    By listing the first six numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    sum = 0
    a, b = 0, 1
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b**2
    return sum

# Problem 8
def fibonacci_sum_of_squares_modulo():
    """
    By listing the first six numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    sum = 0
    a, b = 0, 1
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b**2
    return sum

# Problem 9
def fibonacci_sum_of_squares_modulo_prime():
    """
    By listing the first si