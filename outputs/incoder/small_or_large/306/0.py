
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= 15 (and None if -100 <= n < 15).
    """
    if n < 0:
        return "mouse"
    elif n >= 15:
        return "large"
    else:
        return None

# ______________________________________________________________________________
# Problem 5
# ______________________________________________________________________________

def fibonacci(n):
    """
    Given an integer n, return the nth number in the Fibonacci sequence. 
    
    Fibonacci numbers are defined by the recurrence relation:
    
    Fn = F(n-1) + F(n-2), where F(0) = 1 and F(1) = 1.
    
    For example, F(10) = 55 and F(11) = 89.
    
    What is the first Fibonacci number larger than 1,000,000?
    """
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# ______________________________________________________________________________
# Problem 6
# ______________________________________________________________________________

def fibonacci_iterative(n):
    """
    Given a positive integer n, return the nth number in the Fibonacci sequence using an iterative approach.
    
    Uses the same formula as fibonacci but with an explicit formula for the recurrence relation.
    
    Does not use division.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return a

# ______________________________________________________________________________
# Problem 7
# ______________________________________________________________________________

def lucky_seventh_number(n):
    """
    Given a number n between 1 and 500, find the nth number in the sequence such that Lucky seventh 
    returns True when n is found this way. 
    
    Lucky seventh numbers are defined by the following recurrence relation:
    
    L7n = L7n-1 if n is even
    L7n = L7n+1 if n is odd
    
    For example, L7(3) = L7(2) + L7(1) = L7(1) + L7(0) = 1.
    
    Lucky seventh numbers have the property that every even number greater than 2 has an 
    even Lucky seventh number after it, while every odd number greater than 2 has an odd 
    Lucky seventh number after it. 
    
    For example, L7(10) = L7(9) + L7(8) = L7(7) + L7(6) + L7(5) = L7(4) + L7(3) + L7(2) = L7(1) + L7(0) = 1.