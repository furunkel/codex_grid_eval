
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8 and 9. The sum of these multiples is 37.
    Return the sum of all the multiples of 2, 3 or 5 below 200.
    """    
    return sum([x for x in range(1,200) if x%2==0 or x%3==0 or x%5==0])

def fibonacci():
    """
    The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
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
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    """
    a, b = 1, 1
    index = 2
    while len(str(b)) < 1000:
        a, b = b, a+b
        index += 1
    return index

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
    return max([x*y for x in range(100,1000) for y in range(100,1000) if str(x*y) == str(x*y)[::-1]])

def smallest_multiple():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive