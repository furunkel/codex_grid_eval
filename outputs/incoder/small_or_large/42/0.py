
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 10 and "large" if n >= 15 (and neither if 10 <= n < 15).
    """
    if n < 10:
        return "small"
    elif n >= 15:
        return "large"
    else:
        return "small"

# ______________________________________________________________________________
# Problem 5
# ______________________________________________________________________________
def fibonacci(n):
    """
        Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    return fibs[n]

def fib(n):
    """
        Recursive definition for fibonacci numbers.
    """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib_iter(n):
    """
        Iterative definition for fibonacci numbers.
    """
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
    return a

def fib_slow(n):
    """
        Iterative definition for fibonacci numbers.
    """
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
    return b

def fib_memo(n):
    """
        Memoized version of fibonacci function.
    """
    if n < 2:
        return n
    else:
        if n in fibs:
            return fibs[n]
        else:
            fibs[n] = fib_slow(n)
            return fibs[n]

def fib_memo_iter(n):
    """
        Memoized version of fibonacci function.
    """
    if n < 2:
        return n
    else:
        if n in fibs:
            return fibs[n]
        else:
            fibs[n] = fib_iter(n)
            return fibs[n]

def fib_memo_iter2(n):
    """
        Memoized version of fibonacci function.
    """
    if n < 2:
        return n
    else:
        if n in fibs:
            return fibs[n]
        else:
            fibs[n] = fib_iter2(n)
            return fibs[n]

def fib_memo_iter3(n):
    """
        Memoized version of fibonacci function.
    """
    if n < 2:
        return n
    else:
        if n in fibs:
            return fibs[n]
        else:
            fibs[n] = fib_iter3(n)
            return fibs[n]

def fib_memo_iter4(n):
    """
        Memoized version of fibonacci function.
    """
    if n < 2:
        return n
    else:
        if n in fibs:
            return fibs[n]
        else:
            fibs[n] = fib_iter4(n)
            return fibs[n]

def fib_memo_iter5(n):
    """
        Memoized version of fibonacci function.