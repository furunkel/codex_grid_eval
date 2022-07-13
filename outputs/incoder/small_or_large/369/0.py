
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= 2 (and neither if -100 <= n < 2).
    """
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "small"
    else:
        return "large"

# ______________________________________________________________________________
# Problem 5

def fibonacci(n):
    """
    Given an integer n, return the nth Fibonacci number.
    """
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# ______________________________________________________________________________
# Problem 6

def fibonacci_iterative(n):
    """
    Given an integer n, return the nth Fibonacci number using a recursive approach.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b

# ______________________________________________________________________________
# Problem 7

def prime_or_not_prime(n):
    """
    Given an integer n, return "prime" if the number is prime and "not_prime" otherwise.
    """
    if n == 2:
        return "prime"
    elif n < 2:
        return "not_prime"
    elif n % 2 == 0:
        return "not_prime"
    elif n % 3 == 0:
        return "not_prime"
    else:
        for i in range(5, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return "not_prime"
        return "prime"

# ______________________________________________________________________________
# Problem 8

def fibonacci_memoization(n):
    """
    Given an integer n, return the nth Fibonacci number using a recursive approach and a memoization table.
    """
    memo = {}
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    else:
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        memo[n] = b
        return b

# ______________________________________________________________________________
# Problem 9

def fibonacci_dynamic(n):
    """
    Given an integer n, return the nth Fibonacci number using a recursive approach.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b

# ______________________________________________________________________________
# Problem 10

def fibonacci_memoization_dynamic(n):
    """
    Given an integer n, return the nth Fibonacci number using a recursive approach and a memoization table.
    """
    memo = {}
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_dynamic(n)
    return memo[n]

# ______________________________________________________________________________
# Problem 11

def fibonacci_iterative_dynamic(n):
    """
    Given an integer n, return the nth Fibonacci number using a 