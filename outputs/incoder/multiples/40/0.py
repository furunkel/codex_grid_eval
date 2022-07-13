
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 5, we get 2, 4, 5, 6 and 8. The sum of these multiples is 25.
    Return the sum of all the multiples of 2 or 5 below 1000.
    """    
    sum = 0
    for i in range(1, 1000):
        if i % 2 == 0 or i % 5 == 0:
            sum += i
    return sum

def fibonacci():
    """
    Using two variables, a and b, we can compute and display the nth fibonacci number. 
    """
    a, b = 0, 1
    for i in range(10):
        a, b = b, a + b
        print b
    
def fibonacci_iterative():
    """
    Using a while loop, we can compute and display the nth fibonacci number. 
    """
    a, b = 0, 1
    while a < 10:
        a, b = b, a + b
        print b
        
def fibonacci_memoization():
    """
    Using a memoization table, we can compute and display the nth fibonacci number. 
    """
    memo = {}
    a, b = 0, 1
    while a < 10:
        a, b = b, a + b
        if b not in memo:
            memo[b] = a
        print b
        
def fibonacci_memoization_2():
    """
    Using a memoization table, we can compute and display the nth fibonacci number. 
    """
    memo = {}
    a, b = 0, 1
    while a < 10:
        a, b = b, a + b
        if b not in memo:
            memo[b] = a
        else:
            print memo[b]
        
def fibonacci_memoization_3():
    """
    Using a memoization table, we can compute and display the nth fibonacci number. 
    """
    memo = {}
    a, b = 0, 1
    while a < 10:
        a, b = b, a + b
        if b not in memo:
            memo[b] = a
        else:
            print memo[b]
            
def fibonacci_memoization_4():
    """
    Using a memoization table, we can compute and display the nth fibonacci number. 
    """
    memo = {}
    a, b = 0, 1
    while a < 10:
        a, b = b, a + b
        if b not in memo:
            memo[b] = a
        else:
            print memo[b]
            
def fibonacci_memoization_5():
    """
    Using a memoization table, we can compute and display the nth fibonacci number. 
    """
    memo = {}
    a, b = 0, 1
    while a < 10:
        a, b = b, a + b
        if b not in memo:
            memo[b] = a
        else:
            print memo[b]
            
def 