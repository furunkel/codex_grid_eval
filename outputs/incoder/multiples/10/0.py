
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 600.
    """    
    
    sum = 0
    for n in range(600):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

print(multiples())
</cell>
<text>
Problem 4
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


</text>
<cell>
def primes():
    """
    Sum of all primes below two million
    """
    
    sum = 0
    for n in range(2, 2000000):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            sum += n
    return sum

print(primes())
</cell>
<text>
Problem 5
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutations():
    """
    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
    """
    
    sum = 0
    for n in range(1000000):
        digits = [int(i) for i in str(n)]
        permutation = ''
        for d in digits:
            permutation += str(d)
        sum += int(permutation)
    return sum

print(lexicographic_permutations())
</cell>
<text>
Problem 6
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.
"""


</text>
<cell>
def primes():
    """
    Sum of all primes below two million
    """
    
    sum = 0
    for n in range(2, 2000000):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            sum += n
    return sum

def first_six():
    """
    Sum of first six prime numbers
    """
    
    sum = 0
    for n in range(6):
        sum += primes()
    return sum

print(first_six())
</cell>
<text>
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the sum of the first six prime numbers is 26.
What is the sum of the first seven prime numbers?


</text>
<cell>
def primes():
    """
    Sum of all 