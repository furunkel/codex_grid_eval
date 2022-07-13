
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 124.
    """    
    
    multiples = []
    
    for i in range(12):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
            
    return sum(multiples)

def fibonacci():
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    They are the first two numbers to have two distinct prime factors, namely 1 and 2. 
    By listing the first six numbers of the sequence whose product is 233,
    we can see that the first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5, 8.
    Consequently, 233 is the first non-repeating number in the Fibonacci sequence.
    
    Find the first non-repeating Fibonacci number in the sequence
    """
    
    fibs = []
    
    for i in range(6):
        fibs.append(i)
        
    fibs.sort()
    
    fibs.reverse()
    
    fibs.insert(0, 0)
    fibs.append(1)
    
    fibs.insert(1, 0)
    fibs.append(1)
    
    fibs.insert(2, 0)
    fibs.append(1)
    
    fibs.insert(3, 0)
    fibs.append(1)
    
    fibs.insert(4, 0)
    fibs.append(1)
    
    fibs.insert(5, 0)
    fibs.append(1)
    
    fibs.insert(6, 0)
    fibs.append(1)
    
    fibs.insert(7, 0)
    fibs.append(1)
    
    fibs.insert(8, 0)
    fibs.append(1)
    
    fibs.insert(9, 0)
    fibs.append(1)
    
    fibs.insert(10, 0)
    fibs.append(1)
    
    fibs.insert(11, 0)
    fibs.append(1)
    
    fibs.insert(12, 0)
    fibs.append(1)
    
    fibs.insert(13, 0)
    fibs.append(1)
    
    fibs.insert(14, 0)
    fibs.append(1)
    
    fibs.insert(15, 0)
    fibs.append(1)
    
    fibs.insert(16, 0)
    fibs.append(1)
    
    fibs.insert(17, 0)
    fibs.append(1)
    
    fibs.insert(18, 0)
    fibs.append(1)
    
    fibs.insert(19, 0)
    fibs.append(1)
    
    fibs.insert(20, 0)
    fibs.append(1)
    
    fibs.insert(21, 0)
    fibs.append(1)
    