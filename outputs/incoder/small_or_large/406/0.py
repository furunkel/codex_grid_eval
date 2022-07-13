
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 2 and "house" if n >= 15 (and None if 2 <= n < 15).
    """
    if n < 2:
        return "mouse"
    if n >= 15:
        return "house"
    return None


# ______________________________________________________________________________
# Problem 5


def fibonacci(n):
    """
    Given a number n, return Fibonacci series up to and including n.
    """
    return fibonacci_memo[n] if n in fibonacci_memo else fibonacci_memo[n] = fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n):
    """
    Given a number n, return a list containing the Fibonacci series up to and including n.
    """
    if n < 2:
        return [0]
    if n == 2:
        return [0, 1]
    return fibonacci_memo[n - 2] + [fibonacci_memo[n - 1] + fibonacci_memo[n - 2]]


# ______________________________________________________________________________
# Problem 6


def fibonacci_iterative(n):
    """
    Given a number n, return the nth Fibonacci number.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b


def fibonacci_memo(n):
    """
    Given a number n, return a list containing the nth Fibonacci number.
    """
    if n < 2:
        return [0]
    if n == 2:
        return [0, 1]
    if n in fibonacci_memo:
        return fibonacci_memo[n]
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    fibonacci_memo[n] = b
    return b


# ______________________________________________________________________________
# Problem 7


def power_iterative(n):
    """
    Given a number n, return n^2.
    """
    return n * n


def power_memo(n):
    """
    Given a number n, return a list containing the nth power of the number n.
    """
    if n < 2:
        return [0]
    if n == 2:
        return [1, 1]
    if n in power_memo:
        return power_memo[n]
    power_memo[n] = [n ** 2, n ** 3]
    return power_memo[n]


# ______________________________________________________________________________
# Problem 8


def power_iterative_memo(n):
    """
    Given a number n, return n^2.
    """
    if n < 2:
        return [0]
    if n == 2:
        return [1, 1]
    if n in power_memo:
        return power_memo[n]
    power_memo[n] = [n ** 2, n ** 3]
    return power_memo[n]


def power_memo_iterative(n):
    """
    Given a number n, return n^2.