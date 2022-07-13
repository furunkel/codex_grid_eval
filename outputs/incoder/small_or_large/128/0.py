
def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "house" if n >= -1 (and neither if -100 <= n < -1).
    """
    if n < -100:
        return "small"
    elif n < 0:
        return "house"
    else:
        return "large"

# ______________________________________________________________________________
# Problem 5

def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence
    """
    if n < 2:
        return n
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
    return b

# ______________________________________________________________________________
# Problem 7

def fibonacci_memoization(n):
    """
    Return the nth number in the Fibonacci sequence using dynamic programming
    """
    memo = {}
    def fib(n):
        if n < 2:
            return n
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]
    return fib(n)

# ______________________________________________________________________________
# Problem 8

def fibonacci_memoization_iterative(n):
    """
    Return the nth number in the Fibonacci sequence using dynamic programming
    """
    memo = {}
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b in memo:
            return memo[b]
    return b

# ______________________________________________________________________________
# Problem 9

def fibonacci_memoization_recursive(n):
    """
    Return the nth number in the Fibonacci sequence using dynamic programming
    """
    memo = {}
    def fib(n):
        if n < 2:
            return n
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]
    return fib(n)

# ______________________________________________________________________________
# Problem 10

def fibonacci_memoization_recursive_iterative(n):
    """
    Return the nth number in the Fibonacci sequence using dynamic programming
    """
    memo = {}
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b in memo:
            return memo[b]
        else:
            memo[b] = fib(n - 1) + fib(n - 2)
    return b

# ______________________________________________________________________________
# Problem 11

def fibonac