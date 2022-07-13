
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 3 or 5, we get  and 3. The product of these multiples is 3.
    Return the product of all the multiples of 3 or 5 below 200.
    """    
    return sum([x for x in range(200) if x % 3 == 0 or x % 5 == 0])

def fibonacci():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed 4 million, find the sum of the even-valued terms.
    """
    fib = [1, 2]
    while fib[-1] < 4000000:
        fib.append(fib[-1] + fib[-2])
    return sum([x for x in fib if x % 2 == 0])

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
    return max([x * y for x in range(100, 1000) for y in range(100, 1000) if str(x * y) == str(x * y)[::-1]])

def smallest_multiple():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    n = 20
    while True:
        if all(n % x == 0 for x in range(1, 21)):
            return n
        n += 20

def sum_square_difference():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the