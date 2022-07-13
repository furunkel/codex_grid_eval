
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 1000.
    """    
    
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_below_2million():
    """
    Sum of all primes below 2 million
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(primes_below_2million())
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers in the first ten prime numbers?


</text>
<cell>
def first_ten_primes():
    """
    Sum of first ten prime numbers
    """
    
    sum = 0
    for i in range(2, 101):
        if isprime(i):
            sum += i
    return sum

print(first_ten_primes())
</cell>
<text>
Problem 9
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


</text>
<cell>
def fibonacci_evens():
    """
    Sum of even Fibonacci numbers
    """
    
    sum = 0
    for i in range(1, 4000000):
        if isprime(i):
            if i % 2 == 0:
                sum += i
    return sum

print(fibonacci_evens())
</cell>
<text>
Problem 10
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def largest_palindrome():
    """
    Find the largest palindrome made from the product of two 3-digit numbers
    """
    
    sum = 0
    for i in range(1, 1000000):
        if isprime(i):
            for j in range(1, 1000000):
                if isprime(j):
                    prod = i * j
                    if str(prod) == str(prod)[::-1]:
                        sum += prod
    return sum

print(largest_palindrome())
</cell>
<text>
Problem 11
A palindromic number read