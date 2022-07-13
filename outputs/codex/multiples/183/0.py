
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 13 or 17, we get  and 13. The product of these multiples is 13.
    Return the product of all the multiples of 13 or 17 below 100.
    """    
    return reduce(lambda x,y: x*y, [x for x in range(1,100) if x%13==0 or x%17==0])

def sum_of_squares():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    return sum([x for x in range(1,101)])**2 - sum([x**2 for x in range(1,101)])

def prime_factors():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    return max(prime_factors_of(600851475143))

def prime_factors_of(n):
    """
    Returns a list of prime factors of n
    """
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

def largest_palindrome_product():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return max([x*y for x in range(100,1000) for y in range(100,1000) if str(x*y) == str(x*y)[::-1]])

def smallest_multiple():
    """
   