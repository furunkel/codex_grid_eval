
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5, 3 or 2, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 5, 3 or 2 below 197.
    """    
    
    sum = 0
    
    for n in range(1, 201):
        if n % 5 == 0 or n % 3 == 0 or n % 2 == 0:
            sum += n
            
    return sum
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
def primes():
    """
    Find the sum of all the primes below two million.
    """
    
    sum = 0
    
    for n in range(2, 2000000):
        
        for i in range(2, n):
            
            if n % i == 0:
                break
        else:
            sum += n
            
    return sum
</cell>
<cell>
primes()
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the sum of the first six prime numbers is 2 + 3 + 5 + 7 + 11 + 13 = 55. 
Find the sum of all the first six prime numbers.


</text>
<cell>
def primes():
    """
    Find the sum of all the first six prime numbers.
    """
    
    sum = 0
    
    for n in range(2, 6):
        
        for i in range(2, n):
            
            if n % i == 0:
                break
        else:
            sum += n
            
    return sum
</cell>
<cell>
primes()
</cell>
<text>
Problem 9
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


</text>
<cell>
def fibonacci():
    """
    Find the sum of the even-valued terms in the Fibonacci sequence.
    """
    
    sum = 0
    
    for n in range(2, 4000000):
        
        if n % 2 == 0:
            sum += n
            
    return sum
</cell>
<cell>
fibonacci()
</cell>
<text>
Problem 10
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def palindromes():
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    
    sum = 0
    
    for n in range(2, 999):
        
        for m in range(2, n):