
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 5, we get 2, 4, 5, 6 and 8. The product of these multiples is 1920.
    Return the product of all the multiples of 2 or 5 below 200.
    """    
    
    multiples = []
    for i in range(1, 201):
        if i % 2 == 0 or i % 5 == 0:
            multiples.append(i)
    return sum(multiples)

print(multiples())
</cell>
<text>
Problem 4
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


</text>
<cell>
def primes_sum():
    """
    Sum of primes below two million
    """
    
    primes = []
    for i in range(2, 2000000):
        if isprime(i):
            primes.append(i)
    return sum(primes)

print(primes_sum())
</cell>
<text>
Problem 5
A permutation is a rearrangement of objects into a new order.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


</text>
<cell>
def lexicographic_permutations():
    """
    Lexicographic permutation of digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
    """
    
    permutations = []
    for i in range(0, 1000000):
        permutations.append(str(i))
    return permutations[1000000]

print(lexicographic_permutations())
</cell>
<text>
Problem 6
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.
"""


</text>
<cell>
def primes_sum():
    """
    Sum of primes below two million
    """
    
    primes = []
    for i in range(2, 2000000):
        if isprime(i):
            primes.append(i)
    return sum(primes[:6])

print(primes_sum())
</cell>
<text>
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the sum of the first six prime numbers is 23. 
What is the sum of the first seven prime numbers?
"""


</text>
<cell>
def primes_sum():
    """
    Sum of primes below two million
    """
    
    primes = []
    for i in range(2, 2000000):
        if isprime(i):
            primes.append(i)
    return sum(primes[:7])

print(primes_sum())
</cell>
<text>
Problem 8
By 