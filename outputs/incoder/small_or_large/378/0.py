
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "small" if n >= 15 (and neither if 10 <= n < 15).
    """
    if n < 10:
        return "mouse"
    elif n >= 15:
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
    Given an integer n, return the nth Fibonacci number using an iterative approach.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

# ______________________________________________________________________________
# Problem 7

def primes(n):
    """
    Return a list of the first n prime numbers.
    """
    if n < 2:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [3, 3]
    elif n % 2 == 0:
        return [2]
    elif not n & 1:
        return [2]
    else:
        sieve = [True] * n
        for i in range(3, int(n**0.5) + 1, 2):
            if sieve[i]:
                sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
        return [2] + [2*i+1 for i in range(1,int(n**0.5)+1) if sieve[i]]

# ______________________________________________________________________________
# Problem 8

def primes_sieve(n):
    """
    Return a list of the first n prime numbers.
    """
    if n < 2:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [3, 3]
    elif n % 2 == 0:
        return [2]
    elif not n & 1:
        return [2]
    else:
        sieve = [True] * n
        for i in range(3, int(n**0.5) + 1, 2):
            if sieve[i]:
                sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
        return [2] + [2*i+1 for i in range(1,int(n**0.5)+1) if sieve[i]]

# ______________________________________________________________________________
# Problem 9

def power_digits(n):
    """
    Find the first 10 digits of n's binary representation.
    """
    if n < 10:
        return n
    else:
        return power_digits(n // 10) * 10 + n % 10

# ______________________________________________________________________________
# Problem 10

def power_digit_sum(n):
    """
    Find the sum of the first 10 digits of n's binary representation.
    """
    if n < 10:
        return n
    else:
