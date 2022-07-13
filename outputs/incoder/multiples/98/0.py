
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The sum of these multiples is 29.
    Return the sum of all the multiples of 2 or 9 below 100.
    """    
    
    total = 0
    for i in range(1, 101):
        if i % 2 == 0:
            total += i
        elif i % 9 == 0:
            total += i
    return total

print(multiples())
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_under_2million():
    """
    Find the sum of all the primes below two million.
    """
    
    total = 0
    for i in range(1, 2000000):
        if isprime(i):
            total += i
    return total

print(primes_under_2million())
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers_under_10():
    """
    Find the 10 001st prime number.
    """
    
    total = 0
    for i in range(1, 1000001):
        if isprime(i):
            total += i
    return total

print(prime_numbers_under_10())
</cell>
<text>
Problem 10
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


</text>
<cell>
def fibonacci_sum_under_4_million():
    """
    Find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.
    """
    
    total = 0
    a, b = 0, 1
    for i in range(1, 4000000):
        total += a
        a, b = b, a + b
    return total

print(fibonacci_sum_under_4_million())
</cell>
<text>
Problem 11
By considering the terms in the first one hundred non-abundant numbers, find the sum of the even-valued terms.


</text>
<cell>
def fibonacci_sum_under_1_million():
    """
    Find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed one million.
    """
    
    total = 0
    a, b = 0, 1
    for i in range(1, 1000000):
        total += a
        a, b = b, a + b
    return total

print(fibonacci_sum_under_1_million())
</cell>
<text>
Problem 12
By 