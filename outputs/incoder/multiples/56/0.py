
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8 and 9. The sum of these multiples is 37.
    Return the sum of all the multiples of 5, 3 or 2 below 100.
    """    
    return sum(i for i in range(1, 101) if i%5==0 or i%3==0 or i%2==0)

# Problem 4
def fibonacci():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence.
    """
    return fib

# Problem 5
def fibonacci_iterative():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence.
    """
    a, b = 0, 1
    while b < 20:
        yield b
        a, b = b, a+b

# Problem 6
def fibonacci_memoization():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence.
    """
    cache = {}
    def fib(n):
        if n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return fib

# Problem 7
def fibonacci_memoization_with_generator():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence.
    """
    cache = {}
    def fib(n):
        if n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return fib

# Problem 8
def fibonacci_memoization_with_generator_with_condition():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence.
    """
    cache = {}
    def fib(n):
        if n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        elif n < 20:
            return cache[n]
        else:
            return fib(n-20)
    return fib

# Problem 9
def fibonacci_memoization_with_generator_with_condition_with_if():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence.
    """
    cache = {}
    def fib(n):
        if n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        elif n < 20:
            return cache[n]
        else:
            return fib(n-20)
    return fib

# Problem 10
def fibonacci_memoization_with_generator_with_condition_with_if_with_else():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence.
    """
    cache = {}
    def fib(n):
        if n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        elif n < 20:
            return cache[n]
        else:
            return fib(n-20)
    return fib

# Problem 11
def fibonacci_memoization_with_generator_with_condition_with_