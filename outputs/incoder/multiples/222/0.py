
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 9, we get 2, 4, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 65.
    Return the sum of all the multiples of 2 or 9 below 1000.
    """    
    
    sum = 0
    for i in range(1, 1000):
        if i % 2 == 0:
            sum += i
        elif i % 9 == 0:
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
    Find the sum of all the primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum

print(primes_below(2000000))
</cell>
<text>
Problem 8
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def palindrome(n):
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    
    product = n * n
    
    product = str(product)
    
    product = product[::-1]
    
    if product == product:
        return product
    else:
        return None

print(palindrome(999))
</cell>
<text>
Problem 9
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def million_permutation(n):
    """
    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """
    
    permutations = []
    
    permutations.append(0)
    permutations.append(1)
    permutations.append(2)
    permutations.append(3)
    permutations.append(4)
    permutations.append(5)
    permutations.append(6)
    permutations.append(7)
    permutations.append(8)
    permutations.append(9)
    
    permutations.sort()
    
    permutations.append(n)
    
    return permutations[len(permutations) - 1]

print(million_permutation(9))
</cell>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below 