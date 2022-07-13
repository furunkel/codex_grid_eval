
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The product of these multiples is 8.
    Return the product of all the multiples of 2 or 5 below 197.
    """    
    
    return sum([i for i in range(2, 197) if i % 2 == 0 or i % 5 == 0])

def fibonacci():
    """
    We list the first *n* numbers of the Fibonacci sequence with *n* being any positive integer.
    For example, the *first* 10 numbers in the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
    By starting with 0 and 1, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 1 and 2, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 2 and 3, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 3 and 5, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 5 and 8, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 8 and 13, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 13 and 21, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 21 and 34, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 34 and 55, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 55 and 89, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 89 and 144, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 144, we see that the *first* 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    """
    
    return sum([i for i in range(1, 10) if i % 2 == 0 or i % 5 == 0])

def fibonacci_prime():
    """
    We list the first *n* numbers of the Fibonacci sequence with *n* being any positive integer.
    For example, the *first* 10 numbers in the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
    By starting with 0 and 1, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 1 and 2, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21.
    By starting with 