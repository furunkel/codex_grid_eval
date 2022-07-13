
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 7 or 9, we get 5, 7 and 9. The product of these multiples is 315.
    Return the product of all the multiples of 5, 7 or 9 below 1000.
    """    
    return reduce(lambda x, y: x * y, set(filter(lambda x: x % 5 == 0 or x % 7 == 0 or x % 9 == 0, range(1, 1000))))

def sum_of_squares():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    return sum(range(1, 101)) ** 2 - sum(map(lambda x: x ** 2, range(1, 101)))

def is_palindrome(n):
    """
    Returns True if n is a palindrome, False otherwise.
    """
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return max(filter(is_palindrome, [x * y for x in range(100, 1000) for y in range(100, 1000)]))

def smallest_multiple():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    return reduce(lambda x, y: x * y // gcd(x, y), range(1, 21))

def sum_square_difference():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the