
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 2, 3 or 5 below 200.
    """    
    
    sum = 0
    for i in range(1, 200):
        if i%2==0 or i%3==0 or i%5==0:
            sum = sum + i
    return sum

#Problem 5
def fibonacci():
    """
    By listing the first six terms in the Fibonacci sequence 
    we get 1, 1, 2, 3, 5, 8. The sum of these terms is 23.
    Find the sum of all the even Fibonacci numbers below 10000.
    """
    
    sum = 0
    
    for i in range(1, 10000):
        if i%2==0:
            sum = sum + i
    return sum

#Problem 6
def fibonacci2():
    """
    By considering the terms in the Fibonacci sequence whose 
    first two terms are 1 and 1, we can see that the sum of the 
    even terms is 2. That means 1! + 2! = 2 
    
    By the same method, we can calculate the sum of all the 
    even Fibonacci numbers below 10000.
    """
    
    sum = 0
    
    for i in range(1, 10000):
        if i%2==0:
            sum = sum + i
    return sum

#Problem 7
def fibonacci3():
    """
    By considering the terms in the Fibonacci sequence whose 
    first three terms are 1, 1, and 2, we can see that the sum of the 
    even terms is 3. That means 1! + 2! + 3! = 3 
    
    By the same method, we can calculate the sum of all the 
    even Fibonacci numbers below 10000.
    """
    
    sum = 0
    
    for i in range(1, 10000):
        if i%2==0 or i%3==0:
            sum = sum + i
    return sum

#Problem 8
def fibonacci4():
    """
    By considering the terms in the Fibonacci sequence whose 
    first four terms are 1, 1, 2, and 3, we can see that the sum of the 
    even terms is 6. That means 1! + 2! + 3! + 4! = 6 
    
    By the same method, we can calculate the sum of all the 
    even Fibonacci numbers below 10000.
    """
    
    sum = 0
    
    for i in range(1, 10000):
        if i%2==0 or i%3==0 or i%4==0:
            sum = sum + i
    return sum

#Problem 9
def fibonacci5():
    """
    By considering the terms in the Fibonacci sequence whose 
    first five terms are 1, 1, 2, 3, and 