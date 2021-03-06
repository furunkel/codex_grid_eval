
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5, 3 or 2, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 5, 3 or 2 below 100.
    """    
    sum = 0
    for i in range(1, 101):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum

# Problem 4
def fibonacci():
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a+b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 5
def fibonacci_sum():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a+b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 6
def fibonacci_sum_of_squares():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a+b
        if b % 2 == 0:
            sum += b**2
    return sum

# Problem 7
def fibonacci_sum_of_squares_modulo():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a+b
        if b % 2 == 0:
            sum += b**2
    return sum

# Problem 8
def fibonacci_sum_of_squares_modulo_prime():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a+b
        if b % 2 == 0:
            sum += b**2
    return sum

# Problem 9
def fibonacci_sum_of_squares_modulo_prime_prime():