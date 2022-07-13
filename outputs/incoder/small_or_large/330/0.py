
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 15 (and neither if 10 <= n < 15).
    """
    if n < 10:
        return "mouse"
    elif n >= 15:
        return "large"
    else:
        return "small"

# ______________________________________________________________________________
# Problem 5

def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# ______________________________________________________________________________
# Problem 6

def fibonacci_iterative(n):
    """
    Return the nth number in the Fibonacci sequence
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

# ______________________________________________________________________________
# Problem 7

def fibonacci_memoization(n):
    """
    Return the nth number in the Fibonacci sequence using memoization
    """
    memo = {}
    def fib(n):
        if n not in memo:
            memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
    return fib(n)

# ______________________________________________________________________________
# Problem 8

def fibonacci_dynamic(n):
    """
    Return the nth number in the Fibonacci sequence using dynamic programming
    """
    if n < 2:
        return n
    else:
        return fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)

# ______________________________________________________________________________
# Problem 9

def fibonacci_bottom_up(n):
    """
    Return the nth number in the Fibonacci sequence using bottom up dynamic programming
    """
    if n < 2:
        return n
    else:
        return fibonacci_bottom_up(n - 1) + fibonacci_bottom_up(n - 2)

# ______________________________________________________________________________
# Problem 10

def fibonacci_bottom_up_iterative(n):
    """
    Return the nth number in the Fibonacci sequence using bottom up iterative dynamic programming
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

# ______________________________________________________________________________
# Problem 11

def fibonacci_bottom_up_memoization(n):
    """
    Return the nth number in the Fibonacci sequence using bottom up memoization
    """
    memo = {}
    def fib(n):
        if n not in memo:
            memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
    return fib(n)

# ____________________________________________________________________________