
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 2, 3 or 5 below 197.
    """    
    
    sum = 0
    for i in range(1, 201):
        if i % 2 == 0:
            sum += i
        if i % 3 == 0:
            sum += i
        if i % 5 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 5
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_sum():
    """
    Find the sum of all the primes below two million.
    """    
    
    sum = 0
    for i in range(1, 2000000):
        if isprime(i):
            sum += i
    return sum

print(primes_sum())
</cell>
<text>
Problem 6
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutation():
    """
    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """    
    
    sum = 0
    for i in range(1, 1000000):
        if isprime(i):
            sum += i
    return sum

print(lexicographic_permutation())
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.


</text>
<cell>
def primes_sum():
    """
    Find the sum of the first six prime numbers.
    """    
    
    sum = 0
    for i in range(1, 7):
        if isprime(i):
            sum += i
    return sum

print(primes_sum())
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the sum of the first six prime numbers is 26.
What is the sum of the first seven prime numbers?


</text>
<cell>
def primes_sum():
    """
    Find the sum of the first seven prime numbers.
    """    
    
    sum = 0
    for i in range(1, 7):
        if isprime(i):
            sum += i
    return sum

print(primes_sum())
</cell>
<text>
Problem 9
By listing the 