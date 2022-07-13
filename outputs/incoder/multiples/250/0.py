
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5 or 3, we get  and 3. The sum of these multiples is 3.
    Return the sum of all the multiples of 5 or 3 below 1000.
    """    
    sum = 0
    for i in range(1, 1000):
        if i % 5 == 0 or i % 3 == 0:
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
def prime_sum():
    """
    Find the sum of all the primes below two million.
    """
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

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
    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """
    permutation = ''
    
    for i in range(0, 1000000):
        permutation += str(i)
    
    return permutation

print(lexicographic_permutation())
</cell>
<text>
Problem 9
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.


</text>
<cell>
def prime_sum():
    """
    Find the sum of the first six prime numbers.
    """
    sum = 0
    for i in range(2, 6):
        if isprime(i):
            sum += i
    return sum

print(prime_sum())
</cell>
<text>
Problem 10
The sum of the first ten natural numbers is:  
n(n+1)(2n+1)/6 
= (10!)^1/2 
= (10!)^0.5 
= 10^0.5 
= 10 
Hence the sum of the first ten natural numbers is:  
(1 + 2 + ... + 10)^1/2 = 55.
Find the sum of all the first ten natural numbers below two million.


</text>
<cell>
def first_ten_sum():
    """
    Find the sum of all the first ten natural numbers below two million.
    """
    sum = 0
    for i in range(1, 2000000):
        if isprime(i):
            sum += 