
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The sum of these multiples is 45.
    Return the sum of all the multiples of 5, 7 or 9 below 124.
    """    
    
    sum_of_multiples = 0
    
    for i in range(1, 125):
        if i % 5 == 0 or i % 7 == 0 or i % 9 == 0:
            sum_of_multiples += i
            
    return sum_of_multiples
</cell>
<cell>
multiples()
</cell>
<text>
Problem 4
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def sum_of_primes_under_2_million():
    """
    Sum of all the primes below 2 million
    """
    
    sum_of_primes = 0
    
    for i in range(2, 2000000):
        if isprime(i):
            sum_of_primes += i
            
    return sum_of_primes
</cell>
<cell>
sum_of_primes_under_2_million()
</cell>
<text>
Problem 5
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def largest_palindrome():
    """
    Find the largest palindrome made from the product of two 3-digit numbers
    """
    
    largest_palindrome = 0
    
    for i in range(100, 999):
        for j in range(100, 999):
            product = i * j
            
            if isPalindrome(product):
                if product > largest_palindrome:
                    largest_palindrome = product
                    
    return largest_palindrome
</cell>
<cell>
largest_palindrome()
</cell>
<text>
Problem 6
A palindromic number reads the same both ways. The largest palindrome made from the product of two 3-digit numbers is 906609 = 660 x 998.
Find the largest palindrome made from the product of two 4-digit numbers.


</text>
<cell>
def largest_palindrome():
    """
    Find the largest palindrome made from the product of two 4-digit numbers
    """
    
    largest_palindrome = 0
    
    for i in range(1000, 9999):
        for j in range(1000, 9999):
            product = i * j
            
            if isPalindrome(product):
                if product > largest_palindrome:
                    largest_palindrome = product
                    
    return 