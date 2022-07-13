
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The product of these multiples is 3456.
    Return the product of all the multiples of 2 or 9 below 500.
    """    
    
    multiples = []
    
    for i in range(1, 500):
        if i % 2 == 0:
            multiples.append(i)
        elif i % 9 == 0:
            multiples.append(i)
    
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def sum_of_primes(n):
    """
    Sum of all primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        if i % 2 == 0:
            primes.append(i)
        elif i % 3 == 0:
            primes.append(i)
        elif i % 5 == 0:
            primes.append(i)
        elif i % 7 == 0:
            primes.append(i)
    
    return sum(primes)
</cell>
<cell>
sum_of_primes(2000000)
</cell>
<text>
Problem 8
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutation(n):
    """
    Find the millionth lexicographic permutation of n digits.
    """
    
    permutations = []
    
    for i in range(0, n):
        permutations.append(str(i))
    
    permutations.sort()
    
    return permutations[999999]
</cell>
<cell>
lexicographic_permutation(9)
</cell>
<text>
Problem 9
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.


</text>
<cell>
def sum_of_primes(n):
    """
    Sum of all primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        if i % 2 == 0:
            primes.append(i)
        elif i % 3 == 0:
            primes.append(i)
        elif i % 5 == 0:
            primes.append(i)
        elif i % 7 == 0:
            primes.append(i)
    
    return sum(primes)
</cell>
<cell>
sum_of_primes(6)
</cell>
<text>
Problem 10
A permutation is a rearrangement of objects. For example, 3