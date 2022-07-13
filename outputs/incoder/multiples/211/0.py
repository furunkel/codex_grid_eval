
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 9, we get 2, 4, 6, 8, 9, 10, 12 and 14. The product of these multiples is 5806080.
    Return the product of all the multiples of 2 or 9 below 100.
    """    
    
    multiples = []
    for i in range(1, 101):
        if i % 2 == 0:
            if i % 9 == 0:
                multiples.append(i)
            else:
                multiples.append(i * 3)
        else:
            multiples.append(i * 3)
    return sum(multiples)

# Problem 4
def fibonacci():
    """
    Using math module, find the nth number in the Fibonacci sequence.
    """
    
    fibs = []
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, 100):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[len(fibs) - 1]

# Problem 5
def fibonacci_sum():
    """
    Using math module, find the sum of all numbers in the Fibonacci sequence that are less than 1000.
    """
    
    fibs = []
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, 1000):
        fibs.append(fibs[i-1] + fibs[i-2])
    return sum(fibs)

# Problem 6
def fibonacci_sum_of_squares():
    """
    Using math module, find the sum of all numbers in the Fibonacci sequence that are less than 1000.
    """
    
    fibs = []
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, 1000):
        fibs.append(fibs[i-1] + fibs[i-2])
    return sum(fibs)**2

# Problem 7
def fibonacci_sum_of_cubes():
    """
    Using math module, find the sum of all numbers in the Fibonacci sequence that are less than 1000.
    """
    
    fibs = []
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, 1000):
        fibs.append(fibs[i-1] + fibs[i-2])
    return sum(fibs)**3

# Problem 8
def fibonacci_sum_of_powers():
    """
    Using math module, find the sum of all numbers in the Fibonacci sequence that are less than 1000.
    """
    
    fibs = []
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, 1000):
        fibs.append(fibs[i-1] + fibs[i-2])
    return sum(fibs)**4

# Problem 9
def fibonacci_sum_of_cubes_squares():
    """
    Using math module, find the sum of all numbers in the Fibonacci sequence that are less than 1000.
    """
    
    fibs = []
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, 1000):
        fibs.append(fibs[i-1] + fibs[i-2])
    return sum(fibs)**