
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The product of these multiples is 24.
    Return the product of all the multiples of 2, 3 or 5 below 100.
    """    
    return prod([i for i in range(2, 100) if i % 3 == 0 or i % 5 == 0])

# END PROBLEM 4

# BEGIN PROBLEM 5
def fibonacci():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence. 
    """
    return fib()

def fib():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while a < 20:
        yield a
        a, b = b, a + b

# END PROBLEM 5

# BEGIN PROBLEM 6
def fibonacci_iter():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while a < 20:
        yield a
        a, b = b, a + b

# END PROBLEM 6

# BEGIN PROBLEM 7
def fibonacci_iter2():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while a < 20:
        yield a
        a, b = b, a + b

# END PROBLEM 7

# BEGIN PROBLEM 8
def fibonacci_iter3():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while a < 20:
        yield a
        a, b = b, a + b

# END PROBLEM 8

# BEGIN PROBLEM 9
def fibonacci_iter4():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while a < 20:
        yield a
        a, b = b, a + b

# END PROBLEM 9

# BEGIN PROBLEM 10
def fibonacci_iter5():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while a < 20:
        yield a
        a, b = b, a + b

# END PROBLEM 10

# BEGIN PROBLEM 11
def fibonacci_iter6():
    """
    Using math sequence, return the first 20 numbers in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while a < 20:
        yield a
        a, b = b, a + b

# END 