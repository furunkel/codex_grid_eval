
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 7 or 9, we get 5, 7 and 9. The sum of these multiples is 21.
    Return the sum of all the multiples of 5, 7 or 9 below 197.
    """    
    
    sum = 0
    for i in range(1, 201):
        if i % 5 == 0 or i % 7 == 0 or i % 9 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 8
Write a function that computes the factorial of a number. Do not use recursion.


</text>
<cell>
def factorial(n):
    """
    Compute the factorial of n, a positive integer
    """
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
</cell>
<text>
Problem 9
Write a function that checks whether a passed string is palindrome or not.


</text>
<cell>
def palindrome(s):
    """
    Checks whether the given string is a palindrome
    """
    
    return s == s[::-1]

print(palindrome('noon'))
print(palindrome('racecar'))
print(palindrome('racecars'))
print(palindrome(''))
</cell>
<text>
Problem 10
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def palindrome(s):
    """
    Checks whether the given string is a palindrome
    """
    
    return s == s[::-1]

def largestPalindrome(n):
    """
    Finds the largest palindrome made from the product of two 3-digit numbers
    """
    
    largestPalindrome = 0
    for i in range(1, n):
        for j in range(1, n):
            product = i * j
            if palindrome(str(product)):
                if product > largestPalindrome:
                    largestPalindrome = product
    return largestPalindrome

print(largestPalindrome(99999))
</cell>
<text>
Problem 11
A permutation is a rearrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def permutation(s):
    """
    Finds the milli