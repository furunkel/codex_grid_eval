
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= -1 (and neither if -100 <= n < -1).
    """
    if n < -100:
        return "mouse"
    elif n < 0:
        return "large"
    else:
        return "small"

# ______________________________________________________________________________
# Problem 5

def f(n):
    """
        The Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
    """
    return 1 if n < 2 else f(n-1) + f(n-2)

def fib_iter(n):
    """
        Using an iterator. Compute the first n Fibonacci numbers. 
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

def fib_pre(n):
    """
        Using a recursive function. Compute the nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_pre(n-1) + fib_pre(n-2)

def fib_rec(n):
    """
        Using a recursive function. Compute the first n Fibonacci numbers. 
    """
    return fib_rec_slow(n, 0)

def fib_rec_slow(n, cache):
    """
        Using a recursive function. Compute the first n Fibonacci numbers. 
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib_rec_slow(n-1, cache) + fib_rec_slow(n-2, cache)
            return cache[n]

def fib_rec_fast(n):
    """
        Using a recursive function. Compute the first n Fibonacci numbers. 
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        cache = [0, 1]
        for i in range(2, n):
            cache.append(cache[-1] + cache[-2])
        return cache[n]

def fib_slow(n):
    """
        Using a recursive function. Compute the first n Fibonacci numbers. 
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a+b
        return a

def fib_fast(n):
    """
        Using a recursive function. Compute the first n Fibonacci numbers. 
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        cache = [0, 1]
        for i in range(2, n):
            cache.append(cache[-1] + cache[-2])
        return cache[-1]

def fib_memo(n):
    """
        Using a recursive function. Compute the first n Fibonacci numbers. 
    """
    if n == 0:
        return 0
    elif 