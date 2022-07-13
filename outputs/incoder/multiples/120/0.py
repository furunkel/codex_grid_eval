
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
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
def primes():
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(primes())
</cell>
<text>
Problem 8
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def palindromes():
    sum = 0
    for i in range(1, 10000):
        for j in range(1, 10000):
            if i * j == rev(i * j):
                sum += i * j
    return sum

print(palindromes())
</cell>
<text>
Problem 9
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographics():
    sum = 0
    for i in range(0, 1000000):
        sum += i
    return sum

print(lexicographics())
</cell>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: You may need to consider the sieve of Eratosthenes as well.


</text>
<cell>
def primes():
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

def sieve():
    primes = [True] * 1000000
    primes[0] = False
    primes[1] = False
    primes[2] = False
    primes[3] = False
    primes[4] = False
    primes[5] = False
    primes[6] = False
    primes[7] = False
    primes[8] = False
    primes[9] = False
    for i in range(2, 1000000):
        if primes[i]:
            for j in range(i * i, 1000000