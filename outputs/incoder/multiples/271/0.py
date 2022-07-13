
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The product of these multiples is 24.
    Return the product of all the multiples of 2, 3 or 5 below 197.
    """    
    
    multiples = []
    
    for n in range(2, 197):
        if n % 2 == 0:
            multiples.append(n)
        if n % 3 == 0:
            multiples.append(n)
        if n % 5 == 0:
            multiples.append(n)
    
    return sum(multiples)

def fibonacci():
    """
    Find the n-th number in the Fibonacci sequence. 
    """
    
    fibs = []
    
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, len(fibs)):
        fibs.append(fibs[i-1] + fibs[i-2])
    
    return fibs[len(fibs)-1]

def fibonacci_iterative(n):
    """
    Find the n-th number in the Fibonacci sequence using iteration. 
    """
    
    fibs = []
    
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    
    return fibs[len(fibs)-1]

def fibonacci_memoization(n):
    """
    Find the n-th number in the Fibonacci sequence using memoization. 
    """
    
    fibs = []
    
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    
    return fibs[len(fibs)-1]

def fibonacci_memoization_iterative(n):
    """
    Find the n-th number in the Fibonacci sequence using memoization and iteration. 
    """
    
    fibs = []
    
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    
    return fibs[len(fibs)-1]

def fibonacci_memoization_iterative_memoized(n):
    """
    Find the n-th number in the Fibonacci sequence using memoization, iteration and memoization. 
    """
    
    fibs = []
    
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    
    return fibs[len(fibs)-1]

def fibonacci_memoization_iterative_memoized_iterative(n):
    """
    Find the n-th number in the Fibonacci sequence using memoization, iteration and memoization and iteration. 
    """
    
    fibs = []
    
    fibs.append(0)
    fibs.append(1)
    
    for i in range(2, n):
        fibs.append(fib