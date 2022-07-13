
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 5, 3 or 2 below 500.
    """    
    
    sum = 0
    for i in range(1, 500):
        if i % 5 == 0 and i % 3 == 0:
            sum += i
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes():
    """
    Find the sum of all the primes below two million.
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum
</cell>
<cell>
primes()
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers on the left of the middle five prime numbers?


</text>
<cell>
def sumOfLeftMiddleFivePrimes():
    """
    Find the sum of the numbers on the left of the middle five prime numbers.
    """
    
    sum = 0
    for i in range(2, 6):
        if isprime(i):
            sum += i
    return sum
</cell>
<cell>
sumOfLeftMiddleFivePrimes()
</cell>
<text>
Problem 9
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Hint: consider the terms in the Fibonacci sequence whose values do not exceed four million.

To get the sum of the even-valued terms, you need to sum the numbers on the left of the middle five prime numbers.


</text>
<cell>
def sumOfEvenFibonacciTerms():
    """
    Find the sum of the even-valued terms in the Fibonacci sequence.
    """
    
    sum = 0
    for i in range(2, 4000000):
        if isprime(i):
            sum += i
    return sum
</cell>
<cell>
sumOfEvenFibonacciTerms()
</cell>
<text>
Problem 10
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def largestPalindrome():
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """