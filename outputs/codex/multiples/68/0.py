
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8 and 9. The sum of these multiples is 37.
    Return the sum of all the multiples of 5, 3 or 2 below 1000.
    """    
    return sum(set(range(0, 1000, 5)) | set(range(0, 1000, 3)) | set(range(0, 1000, 2)))

def fibonacci():
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    fib = [1, 2]
    while fib[-1] < 4000000:
        fib.append(fib[-1] + fib[-2])
    return sum(filter(lambda x: x % 2 == 0, fib))

def largest_prime_factor():
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