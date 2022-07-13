
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 5, 3 or 2 below 500.
    """    
    return sum(set(range(0, 500, 2)) | set(range(0, 500, 3)) | set(range(0, 500, 5)))

def fibonacci():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    fib = [1, 2]
    while fib[-1] < 4000000:
        fib.append(fib[-1] + fib[-2])
    return sum(filter(lambda x: x % 2 == 0, fib))

def largest_prime_factor():
    """
    What is the largest prime factor of the number 600851475143 ?
    """
    n = 600851475143
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

def largest_palindrome_product():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return max(filter(lambda x: str(x) == str(x)[::-1], [i * j for i in range(100, 1000) for j in range(100, 1000)]))

def smallest_multiple():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    n = 20
    while True:
        if all(n % i == 0 for i in range(1, 21)):
            return n
        n += 20

def sum_square_difference():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 =