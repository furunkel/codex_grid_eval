
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 2, 3 or 5 below 1000.
    """    
    
    sum = 0
    for i in range(1, 1000):
        if i % 2 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum

# Problem 5
def fibonacci():
    """
    By starting with 1 and 2, the first 10 numbers in the Fibonacci sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 
    Find the sum of all the even Fibonacci numbers below 2 million.
    """
    
    sum = 0
    a, b = 1, 2
    for i in range(2, 2000000):
        if i % 2 == 0:
            sum += a
            a = b
            b = a + b
    return sum

# Problem 6
def fibonacci2():
    """
    By starting with 1 and 2, the first 10 numbers in the Fibonacci sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 
    Find the sum of all the even Fibonacci numbers below 2 million.
    """
    
    sum = 0
    a, b = 1, 2
    for i in range(2, 2000000):
        if i % 2 == 0:
            sum += a
            a = b
            b = a + b
    return sum

# Problem 7
def fibonacci3():
    """
    By starting with 1 and 2, the first 10 numbers in the Fibonacci sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 
    Find the sum of all the even Fibonacci numbers below 2 million.
    """
    
    sum = 0
    a, b = 1, 2
    for i in range(2, 2000000):
        if i % 2 == 0:
            sum += a
            a = b
            b = a + b
    return sum

# Problem 8
def fibonacci4():
    """
    By starting with 1 and 2, the first 10 numbers in the Fibonacci sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 
    Find the sum of all the even Fibonacci numbers below 2 million.
    """
    
    sum = 0
    a, b = 1, 2
    for i in range(2, 2000000):
        if i % 2 == 0:
            sum += a
            a = b
            b = a + b
    return sum

# Problem 9
def fibonacci5():
    """
    By starting with 1 and 2, the first 10 numbers in the Fibonacci sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 
    Find the sum of all the even Fibonacci numbers below 