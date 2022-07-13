
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5 or 3, we get  and 3. The sum of these multiples is 3.
    Return the sum of all the multiples of 5 or 3 below 600.
    """    
    
    sum = 0
    
    for i in range(1, 600):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
            
    return sum
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
def primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    
    for i in range(2, n):
        if isprime(i):
            sum += i
            
    return sum
</cell>
<cell>
primes_below(2000000)
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers in the first ten thousand primes?


</text>
<cell>
def primes_sum(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    
    for i in range(2, n):
        if isprime(i):
            sum += i
            
    return sum
</cell>
<cell>
primes_sum(100000)
</cell>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a nested for loop to sum all the primes below two million.


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
</cell>
<cell>
def primes_sum(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    
    for i in range(2, n):
        if isprime(i):
            sum += i
            
    return sum
</cell>
<cell>
primes_sum(2000000)
</cell>
<text>
Problem 11
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a nested for loop to sum all the primes below two million.


</text>
<cell>
def primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    
    