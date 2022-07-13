
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The sum of these multiples is 29.
    Return the sum of all the multiples of 2 or 9 below 197.
    """    
    
    sum = 0
    for i in range(1, 201):
        if i % 2 == 0 or i % 9 == 0:
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
def primes():
    """
    Find the sum of all the primes below two million.
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(primes())
</cell>
<text>
Problem 6
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def palindromes():
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    
    largest = 0
    for i in range(999, 1001):
        for j in range(999, 1001):
            if str(i) * str(j) == str(i)[::-1] and i * j > largest:
                largest = i * j
    return largest

print(palindromes())
</cell>
<text>
Problem 7
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def permutations():
    """
    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """
    
    million = 0
    
    digits = [str(i) for i in range(10)]
    
    digits_sorted = sorted(digits)
    
    digits_sorted.reverse()
    
    digits_sorted = [str(i) for i in digits_sorted]
    
    digits_sorted.reverse()
    
    digits_sorted = "".join(digits_sorted)
    
    digits_sorted = list(digits_sorted)
    
    digits_sorted = [int(digits_sorted[i:i+10]) for i in range(len(digits_sorted)-1)]
    
    digits_sorted.reverse()
    
    