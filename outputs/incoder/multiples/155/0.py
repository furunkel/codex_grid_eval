
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 2, 3 or 5 below 100.
    """    
    return prod([i for i in range(2,100) if i%2==0 or i%3==0 or i%5==0])

def fibonacci():
    """
    We list the Fibonacci numbers from 0 through 100. We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 and 2584. The product of these numbers is 2331469.
    Return the product of the Fibonacci numbers below 1000.
    """
    return prod([i for i in range(0,100) if i%2==0 or i%3==0 or i%5==0])

def fibonacci_prime():
    """
    We list the Fibonacci numbers from 0 through 100. We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 and 2584. The product of these numbers is 2331469.
    Return the product of the Fibonacci numbers below 1000.
    """
    return prod([i for i in range(0,100) if i%2==0 or i%3==0 or i%5==0 or i%7==0])

def fibonacci_prime_prime():
    """
    We list the Fibonacci numbers from 0 through 100. We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 and 2584. The product of these numbers is 2331469.
    Return the product of the Fibonacci numbers below 1000.
    """
    return prod([i for i in range(0,100) if i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%11==0])

def fibonacci_prime_prime_prime():
    """
    We list the Fibonacci numbers from 0 through 100. We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 and 2584. The product of these numbers is 2331469.
    Return the product of the Fibonacci numbers below 1000.
    """
    return prod([i for i in range(0,100) if i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%11==0 or i%13==0])

def fibonacci_prime_prime_prime_prime():
    """
    We list the Fibonacci numbers from 0 through 100. We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 and 2584. The 