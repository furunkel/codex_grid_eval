
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The product of these multiples is 810.
    Return the product of all the multiples of 3 or 5 below 1000.
    """    
    return sum([i for i in range(1, 1000) if i%3 == 0 or i%5 == 0])

# Problem 5
def fibonacci(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below the number n
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return a

# Problem 6
def fibonacci_sum(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below the number n
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return a

# Problem 7
def fibonacci_sum_of_squares(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below the number n
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return a

# Problem 8
def fibonacci_sum_of_squares_recursive(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below the number n
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_sum_of_squares_recursive(n-1) + fibonacci_sum_of_squares_recursive(n-2)

# Problem 9
def fibonacci_sum_of_squares_iterative(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below the number n
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a+