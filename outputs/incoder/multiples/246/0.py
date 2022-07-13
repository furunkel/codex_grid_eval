
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5 or 3, we get  and 3. The sum of these multiples is 3.
    Return the sum of all the multiples of 5 or 3 below 500.
    """    
    
    sum = 0
    for i in range(1, 500):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
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
def sum_of_primes(n):
    """
    Sum of all primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum
</cell>
<cell>
sum_of_primes(2000000)
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
    
    largest = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j == largest_palindrome(i * j):
                largest = i * j
    return largest
</cell>
<cell>
largest_palindrome(99999)
</cell>
<text>
Problem 9
A palindromic number reads the same both ways. The largest palindrome made from the product of two 3-digit numbers is 906609 = 660 x 990.
Find the largest palindrome made from the product of two 4-digit numbers.


</text>
<cell>
def largest_palindrome(n):
    """
    Find the largest palindrome made from the product of two 4-digit numbers.
    """
    
    largest = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j == largest_palindrome(i * j):
                largest = i * j
    return largest
</cell>
<cell>
largest_palindrome(99999)
</cell>
<text>
Problem 10
A palindromic number reads the same both ways. The largest palindrome made from the product of two 3-digit numbers is 906609 = 660 x 990.
Find the largest palindrome made from the product of two 4-digit numbers.


</text>
<cell>
def largest_palindrome(n):
    """