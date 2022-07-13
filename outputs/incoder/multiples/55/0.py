
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8 and 9. The product of these multiples is 51840.
    Return the product of all the multiples of 2, 3 or 5 below 1000.
    """    
    
    multiples = []
    
    for n in range(2, 1000):
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            multiples.append(n)
    
    return sum(multiples)

def fibonacci():
    """
    Using two variables, a and b, we can compute the first few terms of the Fibonacci sequence. 
    """
    
    a = 0
    b = 1
    
    while b < 100:
        a, b = b, a+b
        
    return b

def fibonacci_iterative():
    """
    Using a variable 'a' to store the previous two terms of the Fibonacci sequence, we can compute the next few terms of the Fibonacci sequence. 
    """
    
    a = 0
    b = 1
    
    while b < 100:
        a, b = b, a+b
        
    return b

def fibonacci_memoization():
    """
    Using a variable 'a' to store the previous two terms of the Fibonacci sequence, we can compute the next few terms of the Fibonacci sequence. 
    """
    
    memo = {}
    
    def fibonacci_memoization(a, b):
        if a not in memo:
            memo[a] = b
        else:
            return memo[a]
    
    return fibonacci_memoization

def fibonacci_memoization_with_cache():
    """
    Using a variable 'a' to store the previous two terms of the Fibonacci sequence, we can compute the next few terms of the Fibonacci sequence. 
    """
    
    memo = {}
    
    def fibonacci_memoization_with_cache(a, b):
        if a not in memo:
            memo[a] = b
        else:
            return memo[a]
    
    return fibonacci_memoization_with_cache

def fibonacci_memoization_with_cache_with_return():
    """
    Using a variable 'a' to store the previous two terms of the Fibonacci sequence, we can compute the next few terms of the Fibonacci sequence. 
    """
    
    memo = {}
    
    def fibonacci_memoization_with_cache_with_return(a, b):
        if a not in memo:
            memo[a] = b
        else:
            return memo[a]
    
    return fibonacci_memoization_with_cache_with_return

def fibonacci_memoization_with_cache_with_return_with_return():
    """
    Using a variable 'a' to store the previous two terms of the Fibonacci sequence, we can compute the next few terms of the Fibonacci sequence. 
    """
    
    memo = {}
    
    def fibonacci_memo