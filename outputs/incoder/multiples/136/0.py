
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 5 or 3 below 600.
    """    
    
    sum = 0
    for i in range(1, 600):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum
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
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum
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
    Lexicographic permutation of n digits.
    """
    
    permutation = ''
    for i in range(n):
        permutation += str(i)
    return permutation
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
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum
</cell>
<cell>
sum_of_primes(6)
</cell>
<text>
Problem 10
The sum of the first ten natural numbers is,
$$1! + 2! + 3! + 4! + 5! + 6! + 7! + 8! + 9! = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 58 + 89 = 87$$
The sum of the first two hundred natural numbers is,
$$1! + 2! + 3! + 4! + 5! + 6! + 7! + 8! + 9! + 10! = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 