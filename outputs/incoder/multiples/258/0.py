
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The sum of these multiples is 6.
    Return the sum of all the multiples of 2 or 5 below 200.
    """    
    
    sum = 0
    for i in range(1, 200):
        if i % 5 == 0 or i % 2 == 0: 
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 5
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_under_2million():
    """
    Find the sum of all the primes below two million.
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(primes_under_2million())
</cell>
<text>
Problem 6
A permutation is a rearrangement of objects into a new order.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutation():
    """
    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """
    
    millionth_lexicographic_permutation = 0
    
    # Your code here
    
    return millionth_lexicographic_permutation

print(lexicographic_permutation())
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.


</text>
<cell>
def primes_under_6():
    """
    Find the sum of the first six prime numbers.
    """
    
    sum = 0
    for i in range(2, 7):
        if isprime(i):
            sum += i
    return sum

print(primes_under_6())
</cell>
<text>
Problem 8
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def palindrome():
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    
    largest = 0
    
    # Your code here
    
    return largest

print(palindrome