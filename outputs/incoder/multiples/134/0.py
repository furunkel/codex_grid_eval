
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 5 or 3 below 500.
    """    
    sum = 0
    for i in range(1, 501):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum

# Problem 4
def fibonacci(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below two million.
    """
    sum = 0
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        sum += b
    return sum

# Problem 5
def fibonacci_iterative(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below two million.
    """
    a, b = 0, 1
    sum = 0
    while b < n:
        a, b = b, a + b
        sum += b
    return sum

# Problem 6
def fibonacci_memoization(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below two million.
    """
    memo = {}
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b not in memo:
            memo[b] = b
    return sum(memo.values())

# Problem 7
def fibonacci_memoization_iterative(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Find the sum of all the even Fibonacci numbers below two million.
    """
    memo = {}
    a, b = 0, 1
    sum = 0
    while b < n:
        a, b = b, a + b
        if b not in memo:
            memo[b] = b
        sum += memo[b]
    return sum

# Problem 8
def fibonacci_memoization_iterative_memo(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 14