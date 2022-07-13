
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The product of these multiples is 3456.
    Return the product of all the multiples of 2 or 9 below 1000.
    """    
    return reduce(lambda x,y: x*y, [x for x in range(1,1000) if x%2==0 or x%9==0])

def sum_of_squares():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    return sum([x for x in range(1,101)])**2 - sum([x**2 for x in range(1,101)])

def prime_factors():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    return max(prime_factors_of(600851475143))

def largest_palindrome_product():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return max([x*y for x in range(100,1000) for y in range(100,1000) if is_palindrome(x*y)])

def smallest_multiple():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    return reduce(lambda x,y: x*y, [x for x in range(1,21) if x not in [2,3,5,7,11,13,17,19]]) * 2 * 3 * 5 * 7 * 11 * 13 * 17 *