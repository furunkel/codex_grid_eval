
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The sum of these multiples is 45.
    Return the sum of all the multiples of 5, 7 or 9 below 500.
    """    
    
    sum = 0
    for n in range(15):
        if n % 5 == 0 or n % 7 == 0 or n % 9 == 0:
            sum += n
    return sum

# Problem 4
def fibonacci():
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946,
    Return the sum of the first ten fibonacci numbers. 
    """
    
    sum = 0
    a, b = 0, 1
    for i in range(10):
        sum += a
        a, b = b, a + b
    return sum

# Problem 5
def fibonacci_sum(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946,
    Return the sum of the first n fibonacci numbers. 
    """
    
    sum = 0
    a, b = 0, 1
    for i in range(n):
        sum += a
        a, b = b, a + b
    return sum

# Problem 6
def fibonacci_sum_of_squares(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946,
    Return the sum of the squares of the first n fibonacci numbers. 
    """
    
    sum = 0
    a, b = 0, 1
    for i in range(n):
        sum += a**2
        a, b = b, a + b
    return sum

# Problem 7
def fibonacci_sum_of_squares_recursive(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946,
    Return the sum of the squares of the first n fibonacci numbers. 
    """
    
    if n < 2:
        return n
    else:
        return fibonacci_sum_of_squares_recursive(n - 1) + fibonacci_sum_of_squares_recursive(n - 2)

# Problem 8
def fibonacci_