
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The sum of these multiples is 6.
    Return the sum of all the multiples of 2 or 5 below 600.
    """    
    
    sum_of_multiples = 0
    for n in range(600):
        if n % 2 == 0 or n % 5 == 0:
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
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for n in range(2, n):
        is_prime = True
        for m in range(2, n):
            if n % m == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

print(sum(primes_below(2000000)))
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
    Return the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """
    
    permutations = []
    
    for m in range(n):
        permutations.append(str(m))
        
    permutations.sort()
    
    return permutations[999999]

print(lexicographic_permutation(9))
</cell>
<text>
Problem 9
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers: 2, 3, 5, 7, 11, and 13.
Find the sum of the first ten prime numbers: 2, 3, 5, 7, 11, 13, 17 and 19.


</text>
<cell>
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for n in range(2, n):
        is_prime = True
        for m in range(2, n):
            if n % m == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

print(sum(primes_below(6)))
print(sum(primes_below(10)))
</cell>
<text>
Problem 10
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed 