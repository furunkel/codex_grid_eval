
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 5, we get 2, 4, 5, 6 and 8. The product of these multiples is 1920.
    Return the product of all the multiples of 2 or 5 below 124.
    """    
    return reduce(lambda x, y: x * y, [x for x in range(1, 124) if x % 2 == 0 or x % 5 == 0])

def sum_of_squares():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    return sum([x for x in range(1, 101)]) ** 2 - sum([x ** 2 for x in range(1, 101)])

def is_palindrome(n):
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return str(n) == str(n)[::-1]

def largest_palindrome():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return max([x * y for x in range(100, 1000) for y in range(100, 1000) if is_palindrome(x * y)])

def smallest_multiple():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    return reduce(lambda x, y: x * y // gcd(x, y), range(1, 21))

def sum_square_difference():
    """
