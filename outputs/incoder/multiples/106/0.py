
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The sum of these multiples is 29.
    Return the sum of all the multiples of 2 or 9 below 500.
    """    
    
    sum_of_multiples = 0
    
    for i in range(500):
        if i % 2 == 0:
            sum_of_multiples += i
        elif i % 9 == 0:
            sum_of_multiples += i
            
    return sum_of_multiples
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
    
    sum_of_primes = 0
    
    for i in range(2000000):
        if isprime(i):
            sum_of_primes += i
            
    return sum_of_primes
</cell>
<cell>
primes_below_2million()
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers_10001():
    """
    Find the 10 001st prime number.
    """
    
    sum_of_primes = 0
    
    for i in range(100000):
        if isprime(i):
            sum_of_primes += i
            
    return sum_of_primes
</cell>
<cell>
prime_numbers_10001()
</cell>
<text>
Problem 10
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers_10001():
    """
    Find the 10 001st prime number.
    """
    
    sum_of_primes = 0
    
    for i in range(100000):
        if isprime(i):
            sum_of_primes += i
            
    return sum_of_primes
</cell>
<cell>
prime_numbers_10001()
</cell>
<text>
Problem 11
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers_10001():
    """
    Find the 10 001st prime number.
    """
    
    sum_of_primes = 0
    
    for i in range(100000):
        if isprime(i):
            sum_of_prime