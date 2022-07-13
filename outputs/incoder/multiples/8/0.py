
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 500.
    """    
    
    sum = 0
    for i in range(1, 500):
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
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        is_prime = True
        for p in primes:
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

What is the sum of the numbers in the first ten thousand primes?


</text>
<cell>
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(sum(primes_below(10000)))
</cell>
<text>
Problem 9
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


</text>
<cell>
def fibonacci(n):
    """
    Generate a list of Fibonacci numbers below n.
    """
    
    fibs = []
    
    if n <= 1:
        return fibs
    
    fibs.append(1)
    fibs.append(1)
    
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    
    return fibs

print(sum(fibonacci(2000000)))
</cell>
<text>
Problem 10
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


</text>
<cell>
def fibonacci(n):
    """
    Generate a list of Fibonacci numbers below n.
    """
    
    fibs = []
    
    if n <= 1:
        return fibs
    
    fibs.append(1)
    fibs.append(1)
    
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])