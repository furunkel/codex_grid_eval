
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 13 or 17, we get  and 13. The sum of these multiples is 13.
    Return the sum of all the multiples of 13 or 17 below 1000.
    """    
    multiples = []
    for i in range(1, 1000):
        if i % 13 == 0 or i % 17 == 0:
            multiples.append(i)
    return sum(multiples)

# Problem 4
def fibonacci(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Write a program to find the sum of first n Fibonacci numbers. 
    """
    fibs = []
    fibs.append(0)
    fibs.append(1)
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return sum(fibs)

# Problem 5
def fibonacci2(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Write a program to find the sum of first n Fibonacci numbers. 
    """
    fibs = []
    fibs.append(0)
    fibs.append(1)
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[-1]

# Problem 6
def fibonacci3(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Write a program to find the sum of first n Fibonacci numbers. 
    """
    fibs = []
    fibs.append(0)
    fibs.append(1)
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[-2]

# Problem 7
def fibonacci4(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    Write a program to find the sum of first n Fibonacci numbers. 
    """
    fibs = []
    fibs.append(0)
    fibs.append(1)
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[-3]

# Problem 8
def fibonacci5(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597