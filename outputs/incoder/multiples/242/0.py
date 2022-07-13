
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5 or 3, we get  and 3. The sum of these multiples is 3.
    Return the sum of all the multiples of 5 or 3 below 197.
    """    
    
    sum = 0
    for i in range(1, 201):
        if i % 5 == 0 or i % 3 == 0:
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
def primes():
    """
    Sum of all primes below two million
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(primes())
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of all the primes below two million?


</text>
<cell>
def primes():
    """
    Sum of all primes below two million
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(primes())
</cell>
<text>
Problem 10
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def palindromes():
    """
    Find the largest palindrome made from the product of two 3-digit numbers
    """
    
    sum = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i * j == i * str(j)[::-1]:
                sum += i * j
    return sum

print(palindromes())
</cell>
<text>
Problem 11
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def permutations():
    """
    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
    """
    
    sum = 0
    for i in range(1, 1000000):
        perm = ''
        for j in range(0, 9):
            perm += str(i)[j % len(str(i))]
        if perm == 