
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5 or 3, we get 3, 5, 6 and 9. The product of these multiples is 810.
    Return the product of all the multiples of 5 or 3 below 500.
    """    
    
    multiples = []
    
    for i in range(500):
        if i % 5 == 0 or i % 3 == 0:
            multiples.append(i)
            
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes():
    """
    We need to find all the primes below two million
    """
    
    primes = []
    
    for i in range(2000000):
        if isprime(i):
            primes.append(i)
            
    return sum(primes)
</cell>
<cell>
primes()
</cell>
<text>
Problem 9
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


</text>
<cell>
def abundants():
    """
    We need to find all the abundant numbers below two million
    """
    
    abundants = []
    
    for i in range(2000000):
        if isprime(i) and isprime(i+i):
            abundants.append(i)
            
    return sum(abundants)
</cell>
<cell>
abundants()
</cell>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.


</text>
<cell>
def primes():
    """
    We need to find all the primes below two million
    """
    
    primes = []
    
    for i in range(2000000):
        if isprime(i):
            primes.append(i)
            
    return sum(prime