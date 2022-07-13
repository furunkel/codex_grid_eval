
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 200.
    """    
    
    multiples = []
    for n in range(1, 201):
        if n % 3 == 0 or n % 5 == 0:
            multiples.append(n)
    return sum(multiples)

print(multiples())
</cell>
<text>
Problem 3
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
(The answer may not be precise; it needs to be an approximation.)


</text>
<cell>
def primes_below(n):
    """
    Generate a list of primes below n.
    
    Primes are numbers greater than 1 that do not divide evenly into n.
    
    Source: https://en.wikipedia.org/wiki/Primality_test
    """
    
    primes = []
    
    # Sieve of Eratosthenes
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    
    # Start at 3 and increment by 2
    # Stop at n / 2
    # Stop at sqrt(n)
    # Stop at sqrt(n) + 1
    
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            primes.append(p)
            
    for p in range(