
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5 or 3, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 5 or 3 below 500.
    """    
    sum = 0
    for i in range(500):
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
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return primes

def sum_primes_below(n):
    """
    Return the sum of all the primes below n.
    """
    
    sum = 0
    for p in primes_below(n):
        sum += p
    return sum

print(sum_primes_below(2000000))
</cell>
<text>
Problem 8
A permutation is a rearrangement of objects into a new order.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutation(n):
    """
    Return the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """
    
    perms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    perms.append(0)
    perms.append(1)
    perms.append(2)
    perms.append(3)
    perms.append(4)
    perms.append(5)
    perms.append(6)
    perms.append(7)
    perms.append(8)
    perms.append(9)
    
    return perms[n]

print(lexicographic_permutation(1000000))
</cell>
<text>
Problem 9
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.


</text>
<cell>
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return primes

def sum_primes_below(n):
    """
    Return the sum of all the primes below n.
    """
    
    sum = 0
    for p in primes_