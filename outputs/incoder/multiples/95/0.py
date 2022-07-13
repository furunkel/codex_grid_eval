
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 7 or 9, we get 5, 7 and 9. The product of these multiples is 315.
    Return the product of all the multiples of 5, 7 or 9 below 600.
    """    
    
    multiples = []
    for n in range(600):
        if n % 5 == 0 or n % 7 == 0 or n % 9 == 0:
            multiples.append(n)
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Problem 4
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes():
    """
    Sum of all the primes below two million.
    """    
    
    primes = []
    for n in range(2000000):
        if n%2 == 0:
            primes.append(n)
    return sum(primes)
</cell>
<cell>
primes()
</cell>
<text>
Problem 5
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutations():
    """
    millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """    
    
    permutations = []
    for n in range(1000000):
        permutations.append(str(n))
    return permutations[999999]
</cell>
<cell>
lexicographic_permutations()
</cell>
<text>
Problem 6
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers: 2, 3, 5, 7.

Hint: Use a sieve of Eratosthenes.


</text>
<cell>
def primes():
    """
    Sum of all the primes below two million.
    """    
    
    primes = []
    for n in range(2000000):
        if n%2 == 0:
            primes.append(n)
    return sum(primes)
</cell>
<cell>
def sieving_sieve(n):
    """
    Sieve of Eratosthenes.
    """    
    
    primes = [True] * (n+1)
    primes[0] = False
    
    for i in range(2, int(n**0.5+1)):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes
</cell>
<cell>
def primes():
    """
    Sum