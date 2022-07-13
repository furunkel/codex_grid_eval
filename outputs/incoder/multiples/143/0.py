
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 5, we get 2, 4, 5, 6, 8, 10, 12 and 14. The product of these multiples is 3225600.
    Return the product of all the multiples of 2 or 5 below 124.
    """    
    
    multiples = []
    for n in range(2, 124):
        if n % 2 == 0:
            if n % 5 == 0:
                multiples.append(n)
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
def sum_primes(n):
    """
    Sum the primes below n.
    """
    
    primes = []
    for n in range(2, n):
        if n % 2 == 0:
            primes.append(2)
        if n % 3 == 0:
            primes.append(3)
        if n % 5 == 0:
            primes.append(5)
        if n % 7 == 0:
            primes.append(7)
    return sum(primes)
</cell>
<cell>
sum_primes(2000000)
</cell>
<text>
Problem 8
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def largest_palindrome(n):
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    
    products = []
    for n in range(2, n):
        if n % 2 == 0:
            products.append(n)
        if n % 3 == 0:
            products.append(n * 3)
    return max(products)
</cell>
<cell>
largest_palindrome(2000000)
</cell>
<text>
Problem 9
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def millionth_lexicographic_permutation(n):
    """
    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """
    
    permutations = []
    for n in range(0, n):
        permutations.append(str(n))
    return permutations[999999]
</cell>
<cell>
millionth_lexicographic_permutation(9)
</cell>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 