
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 9, we get 2 and 4. The sum of these multiples is 6.
    Return the sum of all the multiples of 2 or 9 below 124.
    """    
    
    sum_of_multiples = 0
    for n in range(124, 1, -1):
        if n % 2 == 0:
            sum_of_multiples += n
        elif n % 9 == 0:
            sum_of_multiples += n
    return sum_of_multiples

print(multiples())
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def prime_sum():
    """
    Sum of primes below two million
    """
    
    sum_of_primes = 0
    for n in range(2, 2000000):
        if all(n % i for i in range(3, n, 2)):
            sum_of_primes += n
    return sum_of_primes

print(prime_sum())
</cell>
<text>
Problem 8
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutation():
    """
    millionth lexicographic permutation
    """
    
    millionth_lexicographic_permutation = 0
    for n in range(0, 1000000):
        millionth_lexicographic_permutation += n
    return millionth_lexicographic_permutation

print(lexicographic_permutation())
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers():
    """
    10 001st prime number
    """
    
    prime_number = 0
    for n in range(0, 100000):
        prime_number += n
    return prime_number

print(prime_numbers())
</cell>
<text>
Problem 10
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9