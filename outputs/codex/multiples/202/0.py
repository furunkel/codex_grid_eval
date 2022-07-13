
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The sum of these multiples is 45.
    Return the sum of all the multiples of 5, 7 or 9 below 200.
    """    
    return sum(set(range(5, 200, 5)) | set(range(7, 200, 7)) | set(range(9, 200, 9)))

def sum_of_squares():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    return sum(range(1, 101))**2 - sum(x**2 for x in range(1, 101))

def prime_factors():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
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
    return max(x * y for x in range(100, 1000) for y in range(100, 1000) if str(x * y) == str(x * y)[::-1])

def smallest_multiple():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
