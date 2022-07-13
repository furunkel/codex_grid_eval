
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8 and 9. The sum of these multiples is 37.
    Return the sum of all the multiples of 2, 3 or 5 below 100.
    """    
    
    sum = 0
    for i in range(1, 101):
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
Problem 9
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
Problem 10
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutation(n):
    """
    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """
    
    permutations = []
    
    for i in range(0, n):
        permutations.append(i)
        
    permutations.sort()
    
    return permutations[999999]

print(lexicographic_permutation(10))
</cell>
<text>
Problem 11
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.


</text>
<cell>
def prime_sum(n):
    """
    Find the sum of the first n prime numbers.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum

print(prime_sum(6))
</cell>
<text>
Problem 12
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutation(n):
    """
    Find the millionth lexico