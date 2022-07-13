
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 100.
    """    
    
    sum = 0
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum

print(primes_below(2000000))
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum

print(primes_below(1000001))
</cell>
<text>
Problem 10
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum

print(primes_below(10000001))
</cell>
<text>
Problem 11
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum

print(primes_below(1000000001))
</cell>
<text>
Problem 12
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum

