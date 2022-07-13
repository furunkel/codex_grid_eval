
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 124.
    """    
    
    sum = 0
    for i in range(1, 125):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
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
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(sum(primes_below(2000000)))
</cell>
<text>
Problem 5
A permutation is a rearrangement of objects into a new order.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutation(n):
    """
    Generate a list of lexicographic permutations up to n.
    """
    
    permutations = []
    
    for i in range(n):
        permutations.append(i)
        
    for i in range(n - 1):
        j = i + 1
        while j < n:
            permutations[j], permutations[i] = permutations[i], permutations[j]
            j += 1
    return permutations

print(lexicographic_permutation(1000000))
</cell>
<text>
Problem 6
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.
"""


</text>
<cell>
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(sum(primes_below(6)))
</cell>
<text>
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the sum of the first six prime numbers is 26.
What is the sum of the first seven prime numbers?


</text>
<cell>
def primes_below(n):
    """
    Generate a list of primes 