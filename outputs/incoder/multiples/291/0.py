
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5, 3 or 2, we get 2, 3 and 4. The product of these multiples is 24.
    Return the product of all the multiples of 5, 3 or 2 below 600.
    """    
    
    multiples = []
    
    for n in range(600):
        if n % 5 == 0 or n % 3 == 0 or n % 2 == 0:
            multiples.append(n)
            
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
def primes_below_2million():
    """
    Find the sum of all the primes below two million.
    """
    
    primes = []
    
    for n in range(2000000):
        if primes_below_2million.is_prime(n):
            primes.append(n)
            
    return sum(primes)
</cell>
<cell>
primes_below_2million()
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?


</text>
<cell>
def primes_below_10001():
    """
    Find the 10001st prime number.
    """
    
    primes = []
    
    for n in range(1000):
        if primes_below_10001.is_prime(n):
            primes.append(n)
            
    return primes[999]
</cell>
<cell>
primes_below_10001()
</cell>
<text>
Problem 10
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

HINT: What is the smallest prime number that is evenly divisible by all of the numbers from 1 to 20?


</text>
<cell>
def primes_below_10001():
    """
    Find the 10001st prime number.
    """
    
    primes = []
    
    for n in range(1000):
        if primes_below_10001.is_prime(n):
            primes.append(n)
            
    return primes[999]
</cell>
<cell>
primes_below_10001()
</cell>
<text>
Problem 11
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

HINT: What is the smallest prime number that is evenly divisible by all of the numbers from 1 to 1000?


</text>
<cell>
def primes_below_10001():
    """