
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8 and 9. The sum of these multiples is 37.
    Return the sum of all the multiples of 5, 3 or 2 below 200.
    """    
    return sum(set(range(0, 200, 2)) | set(range(0, 200, 3)) | set(range(0, 200, 5)))

def fibonacci():
    """
    The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.
    What is the first term in the Fibonacci sequence to contain 1000 digits?
    """
    a, b = 1, 1
    i = 2
    while len(str(b)) < 1000:
        a, b = b, a + b
        i += 1
    return i

def palindrome():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return max([x * y for x in range(100, 1000) for y in range(100, 1000) if str(x * y) == str(x * y)[::-1]])

def smallest_multiple():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    return reduce(lcm, range(1, 21))

def sum_square_difference():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10