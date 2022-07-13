
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2000 (and neither if -100 <= n < 2000).
    """
    if n < -100:
        return "small"
    elif n >= 2000:
        return "large"
    else:
        return "house"

# ______________________________________________________________________________
# Problem 5
def f(n):
    """
        The Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
    """
    return n if n < 2 else f(n-1) + f(n-2)

def fib_iter(n):
    """
        Using an iterator to compute the Fibonacci sequence. 
    """
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a+b

def fib_pre(n):
    """
        Using two recursive functions to compute the Fibonacci sequence. 
    """
    return fib_rec(n) if n < 2 else fib_rec(n - 1) + fib_rec(n - 2)

def fib_rec(n):
    """
        Using a single recursive function to compute the Fibonacci sequence. 
    """
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

def fib_memo(n):
    """
        Using a recursive function to compute the Fibonacci sequence, memoizing the result. 
    """
    mem = {}
    if n not in mem:
        mem[n] = fib_rec(n)
    return mem[n]

def fib_dyn(n):
    """
        Using a recursive function to compute the Fibonacci sequence, memoizing the result, and using an iterative 
        process to compute the sequence. 
    """
    mem = {}
    if n not in mem:
        mem[n] = fib_iter(n)
    return mem[n]

def fib_dyn2(n):
    """
        Using a recursive function to compute the Fibonacci sequence, memoizing the result, and using an iterative 
        process to compute the sequence. 
    """
    mem = {}
    if n not in mem:
        mem[n] = fib_pre(n)
    return mem[n]

def fib_dyn3(n):
    """
        Using a recursive function to compute the Fibonacci sequence, memoizing the result, and using an iterative 
        process to compute the sequence. 
    """
    mem = {}
    if n not in mem:
        mem[n] = fib_memo(n)
    return mem[n]

def fib_dyn4(n):
    """
        Using a recursive function to compute the Fibonacci sequence, memoizing the result, and using an iterative 
        process to compute the sequence. 
    """
    mem = {}
    if n not in mem:
        mem[n] = fi