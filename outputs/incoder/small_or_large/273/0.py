
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2 (and neither if -100 <= n < 2).
    """
    if n < -100:
        return "large"
    elif n >= 2:
        return "house"
    else:
        return "small"

# ______________________________________________________________________________
# Problem 5

def f(n):
    """
        The Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    return 1 if n < 2 else f(n-1) + f(n-2)

def fib(n):
    """
        The nth number in the Fibonacci sequence
    """
    return f(n)

def fib_iter(n):
    """
        Iterative implementation of the fibonacci sequence
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

def fib_oneline(n):
    """
        Oneline version of the fibonacci sequence
    """
    return next(fib_iter(n))

def fib_memo(n):
    """
        Memorization of the fibonacci sequence
    """
    memo = {}
    def fib(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return fib(n)

def fib_memo_iter(n):
    """
        Iterative implementation of the fibonacci sequence using memoization
    """
    memo = {}
    def fib(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return fib(n)

def fib_memo_oneline(n):
    """
        Oneline version of the fibonacci sequence using memoization
    """
    return next(fib_memo_iter(n))

def fib_largest_series(n):
    """
        The nth number in the Fibonacci sequence which has the largest series
    """
    return max(fib_iter(n))

def fib_largest_series_iter(n):
    """
        Iterative implementation of the fibonacci sequence which has the largest series
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

def fib_largest_series_oneline(n):
    """
        Oneline version of the fibonacci sequence which has the largest series
    """
    return max(fib_largest_series_iter(n))

def fib_largest_series_memo(n):
    """
        Memorization of the fibonacci sequence which has the largest series
    """
    memo = {}
    def fib(n):
        if n not in memo:
            memo[n] = fib_largest_series(n)
        return memo[n]
    return fib(n)

def fib_