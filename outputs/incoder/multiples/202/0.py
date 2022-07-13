
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The sum of these multiples is 45.
    Return the sum of all the multiples of 5, 7 or 9 below 200.
    """    
    
    sum = 0
    for i in range(1, 200):
        if i % 5 == 0 or i % 7 == 0 or i % 9 == 0:
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
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        is_prime = True
        for p in range(2, i):
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(sum(primes_below(2000000)))
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        is_prime = True
        for p in range(2, i):
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(prime_numbers_below(1000000)[0])
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        is_prime = True
        for p in range(2, i):
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(prime_numbers_below(1000000)[0])
</cell>
<text>
Problem 10
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        is_prime = True
        for p in range(2, i):
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)