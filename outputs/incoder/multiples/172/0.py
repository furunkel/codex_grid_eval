
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 5, 3 or 2 below 197.
    """    
    
    sum = 0
    
    for n in range(1, int(math.sqrt(197))+1):
        if n % 5 == 0 or n % 3 == 0 or n % 2 == 0:
            sum += n
            
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def sum_of_primes(n):
    """
    Sum of all the primes below n.
    """
    
    sum = 0
    
    for n in range(2, int(math.sqrt(n))+1):
        if n % 2 == 0:
            sum += n
            
    return sum
</cell>
<cell>
sum_of_primes(2000000)
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers on the left of the middle five prime numbers?


</text>
<cell>
def sum_of_left_five(n):
    """
    Sum of the numbers on the left of the middle five prime numbers.
    """
    
    sum = 0
    
    for n in range(2, n+1):
        if n % 5 == 0:
            sum += n
            
    return sum
</cell>
<cell>
sum_of_left_five(2000000)
</cell>
<text>
Problem 10
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


</text>
<cell>
def sum_of_even(n):
    """
    Sum of the even-valued terms.
    """
    
    sum = 0
    
    for n in range(2, n+1):
        if n % 2 == 0:
            sum += n
            
    return sum
</cell>
<cell>
sum_of_even(2000000)
</cell>
<text>
Problem 11
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the odd-valued terms.


</text>
<cell>
def sum_of_odd(n):
    """
    Sum of the odd-valued terms.
    """
    
    sum = 0
    
    for n in range(2, n+1):
        if n % 2 != 0:
            sum += n
            
    return sum
</cell>
<cell>
sum_of_odd(2000000)
</cell>
<text>
Problem 12
A palindromic number reads the same both way