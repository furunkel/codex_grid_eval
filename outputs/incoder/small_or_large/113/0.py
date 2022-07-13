
def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "small"
    elif n >= 2:
        return "house"
    else:
        return None


# ______________________________________________________________________________
# Problem 5
# ______________________________________________________________________________


def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence. Fibonacci numbers are defined by the recurrence Tn = Tn−1 + Tn−2, where T0 = 1 and T1 = 1.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ______________________________________________________________________________
# Problem 6
# ______________________________________________________________________________


def fibonacci_iterative(n):
    """
    Return the nth number in the Fibonacci sequence. Fibonacci numbers are defined by the recurrence Tn = Tn−1 + Tn−2, where T0 = 1 and T1 = 1.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b


# ______________________________________________________________________________
# Problem 7
# ______________________________________________________________________________


def lucky_seventh_number(n):
    """
    Find the nth number in the Fibonacci sequence that has the property that 7n+1 = 8n. In other words, find the 7th Fibonacci number whose
    value is 8n. Luckily, the 7th Fibonacci number is given by lucky_seventh_number(8) = 17.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b


# ______________________________________________________________________________
# Problem 8
# ______________________________________________________________________________


def fibonacci_memoization(n):
    """
    Find the nth number in the Fibonacci sequence that has the property that 7n+1 = 8n. In other words, find the 7th Fibonacci number whose
    value is 8n. Luckily, the 7th Fibonacci number is given by lucky_seventh_number(8) = 17.
    """
    memo = {}
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return memo[n]


# ______________________________________________________________________________
# Problem 9
# ______________________________________________________________________________


def fibonacci_memoization_iterative