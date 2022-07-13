
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The sum of these multiples is 45.
    Return the sum of all the multiples of 5, 7 or 9 below 100.
    """    
    
    sum_of_multiples = 0
    
    for n in range(1, 101):
        if n % 5 == 0 or n % 7 == 0 or n % 9 == 0:
            sum_of_multiples += n
            
    return sum_of_multiples

print(multiples())
</cell>
<text>
Problem 5
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_below_2million():
    """
    Find the sum of all the primes below two million.
    """
    
    sum_of_primes = 0
    
    for n in range(2, 2000000):
        
        for p in range(2, n):
            
            if n % p == 0:
                break
        else:
            sum_of_primes += n
            
    return sum_of_primes

print(primes_below_2million())
</cell>
<text>
Problem 6
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def largest_palindrome():
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    
    largest_palindrome = 0
    
    for n in range(100, 1000):
        
        for m in range(100, 1000):
            
            if n * m == str(n * m):
                if n * m > largest_palindrome:
                    largest_palindrome = n * m
                    
    return largest_palindrome

print(largest_palindrome())
</cell>
<text>
Problem 7
A palindromic number reads the same both ways. The largest palindrome made from the product of two 3-digit numbers is 906609 = 660 x 990.
Find the largest palindrome made from the product of two 4-digit numbers.


</text>
<cell>
def largest_palindrome():
    """
    Find the largest palindrome made from the product of two 4-digit numbers.
    """
    
    largest_palindrome = 0
    
    for n in range(1000, 10000):
        
        for m in range(1000, 10000):
            
            if n * m == str(n * m):
                if n * m > largest_palindrome:
                    largest_palindrome = n * m
                    
    return largest_palindrome

print(largest_palindro