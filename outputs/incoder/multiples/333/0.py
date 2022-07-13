
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 9, we get 2 and 4. The product of these multiples is 8.
    Return the product of all the multiples of 2 or 9 below 600.
    """    
    
    return sum([i for i in range(2, 600) if i % 2 == 0 or i % 9 == 0])

print(multiples())
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
HINT: You may want to use Project Euler's Sieve of Eratosthenes algorithm. You'll need to do some research to figure out the best way to implement the Sieve of Eratosthenes.


</text>
<cell>
def primes():
    """
    Project Euler problem 7
    """
    
    primes = [i for i in range(2, 2000000) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0]
    
    return sum(primes)

print(primes())
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?


</text>
<cell>
def prime_numbers():
    """
    Project Euler problem 8
    """
    
    primes = [i for i in range(2, 10001) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0 and i % 13 != 0]
    
    return primes[10001-1]

print(prime_numbers())
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

$2^6 - 2^5 - 2^4 - 2^3 - 2^2 - 2^1 = 10001$


</text>
<cell>
def prime_numbers():
    """
    Project Euler problem 9
    """
    
    primes = [i for i in range(2, 10001) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0 and i % 13 != 0]
    
    return 2**6 - 2**5 - 2**4 - 2**3 - 2**2 - 2**1

print(prime_numbers())
</cell>
<text>
Problem 10
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

$2^6 - 2^5 - 2^4 - 2^3 - 2^2 - 2^1 = 10001$

$2^6 - 2^5 - 2^4 - 2^3 - 2^2 - 2^1 = 10001$

$2^6 - 2^5 - 2^4 - 2^3 - 2^2 - 2^1 = 100