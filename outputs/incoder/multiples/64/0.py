
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8 and 9. The sum of these multiples is 37.
    Return the sum of all the multiples of 5, 3 or 2 below 500.
    """    
    return sum([i for i in range(1, 500) if i%5==0 or i%3==0 or i%2==0])

# Problem 3
def fibonacci(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below 2 million.
    """
    return sum([i for i in range(1, n) if i%2==0])

# Problem 4
def fibonacci2(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below 2 million.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return a

# Problem 5
def fibonacci3(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below 2 million.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return a

# Problem 6
def fibonacci4(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below 2 million.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return a

# Problem 7
def fibonacci5(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below 2 million.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return a

# Problem 8
def fibonacci6(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    