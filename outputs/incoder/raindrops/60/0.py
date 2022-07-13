
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 3 or 5, so the result would be "Plong".
    15 has both 3 and 5 as factors, but not 11, so the result would be "PlingBuzz".
    2 is not factored by 3, 5, or 11, so the result would be "2".
    """
    if num % 3 == 0:
        return "Pling"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 11 == 0:
        return "Plong"
    else:
        return str(num)

# END PROBLEM 3


# PROBLEM 4
def fibonacci(n):
    """
    Write a function that returns the nth number in the Fibonacci sequence.
    Use recursion to solve this problem.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# END PROBLEM 4


# PROBLEM 5
def fibonacci_recursive(n):
    """
    Write a function that returns the nth number in the Fibonacci sequence.
    Use recursion to solve this problem.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# END PROBLEM 5


# PROBLEM 6
def fibonacci_iterative(n):
    """
    Write a function that returns the nth number in the Fibonacci sequence.
    Use recursion to solve this problem.
    """
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


# END PROBLEM 6


# PROBLEM 7
def fibonacci_memoization(n):
    """
    Write a function that returns the nth number in the Fibonacci sequence.
    Use recursion to solve this problem.
    """
    memo = {}
    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
        return memo[n]


# END PROBLEM 7


# PROBLEM 8
def fibonacci_memoization_iterative(n):
    """
    Write a function that returns the nth number in the Fibonacci sequence.
    Use recursion to solve this problem.
    """
    memo = {}
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = a
        return memo[n]


# END PROBLEM 8


# PROBLEM 9
def fibonacci_memo