
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8 and 9. The sum of these multiples is 37.
    Return the sum of all the multiples of 5, 3 or 2 below 1000.
    """    
    
    sum = 0
    for i in range(1, 1000):
        if i % 5 == 0 and i % 3 == 0:
            sum += i
    return sum

# Problem 4
def fibonacci():
    """
    By starting with 1 and 2, the first 10 numbers are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610.
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 5
def fibonacci2():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 6
def fibonacci3():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 7
def fibonacci4():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 8
def fibonacci5():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 9
def fibonacci6():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the 