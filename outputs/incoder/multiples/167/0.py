
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 2, 3 or 5 below 1000.
    """    
    
    multiples = []
    for n in range(2, 1000):
        if n % 2 == 0:
            if n % 3 == 0:
                if n % 5 == 0:
                    multiples.append(n)
    return sum(multiples)

# Problem 5
def fibonacci(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    
    Each new term in the sequence is the sum of the previous two terms.
    
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
    
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Problem 6
def fibonacci2(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    
    Each new term in the sequence is the sum of the previous two terms.
    
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
    
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Problem 7
def fibonacci3(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    
    Each new term in the sequence is the sum of the previous two terms.
    
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
    
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(