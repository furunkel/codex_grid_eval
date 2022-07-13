
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The product of these multiples is 8.
    Return the product of all the multiples of 2 or 5 below 124.
    """    
    return reduce(lambda x, y: x * y, [x for x in range(1, 124) if x % 2 == 0 or x % 5 == 0])

def fibonacci():
    """
    The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number.
    """
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    return fib(10)

def sum_of_squares():
    """
    Write a function that takes in an integer n and returns the sum of all squares up to and including n.
    """
    return reduce(lambda x, y: x + y, [x ** 2 for x in range(1, 11)])

def sum_of_odd_squares():
    """
    Write a function that takes in an integer n and returns the sum of all odd squares up to and including n.
    """
    return reduce(lambda x, y: x + y, [x ** 2 for x in range(1, 11) if x % 2 != 0])

def sum_of_odd_cubes():
    """
    Write a function that takes in an integer n and returns the sum of all odd cubes up to and including n.
    """
    return reduce(lambda x, y: x + y, [x ** 3 for x in range(1, 11) if x % 2 != 0])

def sum_of_odd_fibonacci():
    """
    Write a function that takes in an integer n and returns the sum of all odd Fibonacci numbers up to and including n.
    """
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    return reduce(lambda x, y: x + y