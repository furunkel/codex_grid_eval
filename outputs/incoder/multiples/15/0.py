
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5 or 3, we get 3, 5, 6 and 9. The product of these multiples is 810.
    Return the product of all the multiples of 5 or 3 below 100.
    """    
    
    numbers = []
    
    for num in range(0, 100):
        if num % 5 == 0 or num % 3 == 0:
            numbers.append(num)
            
    return sum(numbers)
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
def sum_of_primes(n):
    """
    Sum of all primes below n.
    """
    
    numbers = []
    
    for num in range(2, n):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                numbers.append(num)
                
    return sum(numbers)
</cell>
<cell>
sum_of_primes(2000000)
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a Sieve of Eratosthenes or a Sieve of Atkin.


</text>
<cell>
def sum_of_primes(n):
    """
    Sum of all primes below n.
    """
    
    numbers = []
    
    for num in range(2, n):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                numbers.append(num)
                
    return sum(numbers)
</cell>
<cell>
sum_of_primes(2000000)
</cell>
<text>
Problem 9
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def largest_palindrome(n):
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    
    numbers = []
    
    for num in range(0, n):
        if num % 100 == 0 or num % 10 == 0:
            numbers.append(num)
            
    return max(numbers)
</cell>
<cell>
largest_palindrome(2000000)
</cell>
<text>
Problem 10
A palindromic number reads the same both ways. The largest palindrome made from the product of two 3-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 4-digit numbers.


