
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5 or 3, we get  and 3. The product of these multiples is 3.
    Return the product of all the multiples of 5 or 3 below 600.
    """    
    return sum([i for i in range(1, 600) if i % 5 == 0 or i % 3 == 0])

def fibonacci():
    """
    Using two variables, a and b, we can compute and return the nth number in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while b < 600:
        a, b = b, a+b
    return b

def fibonacci_iterative():
    """
    Using two variables, a and b, we can compute and return the nth number in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while b < 600:
        a, b = b, a+b
    return b

def fibonacci_memoization():
    """
    Using two variables, a and b, we can compute and return the nth number in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while b < 600:
        a, b = b, a+b
    return b

def fibonacci_memoization_with_memo():
    """
    Using two variables, a and b, we can compute and return the nth number in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while b < 600:
        a, b = b, a+b
    return b

def fibonacci_memoization_with_memo_iterative():
    """
    Using two variables, a and b, we can compute and return the nth number in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while b < 600:
        a, b = b, a+b
    return b

def fibonacci_memoization_with_memo_iterative_memo():
    """
    Using two variables, a and b, we can compute and return the nth number in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while b < 600:
        a, b = b, a+b
    return b

def fibonacci_memoization_with_memo_iterative_memo_memo():
    """
    Using two variables, a and b, we can compute and return the nth number in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while b < 600:
        a, b = b, a+b
    return b

def fibonacci_memoization_with_memo_iterative_memo_memo_memo():
    """
    Using two variables, a and b, we can compute and return the nth number in the Fibonacci sequence. 
    """
    a, b = 0, 1
    while b < 600:
        a, b = b, a+b
    return b

def fibonacci_memoization_with_memo_iterative_memo