
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 9, we get 2, 4, 6, 8, 9, 10, 12 and 14. The product of these multiples is 5806080.
    Return the product of all the multiples of 2 or 9 below 600.
    """    
    
    multiples = []
    for i in range(1, 600):
        if i % 2 == 0:
            if i % 9 == 0:
                multiples.append(i)
            else:
                continue
        else:
            if i % 9 == 0:
                continue
            else:
                multiples.append(i)
    return sum(multiples)

def fibonacci():
    """
    Using two recursive functions, implement a function that returns the n-th number in the Fibonacci sequence. 
    """
    
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    return fib(int(input("Enter the number for Fibonacci: ")))

def fibonacci2(n):
    """
    Using a while loop, implement a function that returns the n-th number in the Fibonacci sequence. 
    """
    
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
    return a

def fibonacci3(n):
    """
    Using a recursive function, implement a function that returns the n-th number in the Fibonacci sequence. 
    """
    
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    return fib(n)

def fibonacci4(n):
    """
    Using a recursive function, implement a function that returns the n-th number in the Fibonacci sequence. 
    """
    
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    return fib(n)

def fibonacci5(n):
    """
    Using a recursive function, implement a function that returns the n-th number in the Fibonacci sequence. 
    """
    
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    return fib(n)

def fibonacci6(n):
    """
    Using a recursive function, implement a function that returns the n-th number in the Fibonacci sequence. 
    """
    
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    return fib(n)

def fibonacci7(n):
    """
    Using a recursive function, implement a function that returns the n-th number in the Fibonacci sequence. 
    """
    
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
