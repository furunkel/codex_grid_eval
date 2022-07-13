
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 9, we get 2, 4, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 65.
    Return the sum of all the multiples of 2 or 9 below 600.
    """    
    return sum(i for i in range(1, 600) if i%2 == 0 or i%9 == 0)

#print(multiples())
</cell>
<text>
Problem 3
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_below_2million():
    """
    Find the sum of all the primes below two million.
    """
    
    sum_of_primes = 0
    
    for i in range(2, 2000000):
        
        is_prime = True
        
        for divisor in range(2, i):
            if i%divisor == 0:
                is_prime = False
                break
        
        if is_prime:
            sum_of_primes += i
            
    return sum_of_primes
    
#print(primes_below_2million())
</cell>
<text>
Problem 4
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


</text>
<cell>
def abundant_numbers():
    """
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    """
    
    sum_of_abundant_numbers = 0
    
    for i in range(1, 28123):
        
        is_abundant = True
        
        for divisor in range(2, i):
            if i%divisor == 0:
                is_abundant = False
                break
        
        if is_abundant:
            sum_of_abundant_numbers += i
            
    return sum_of_abundant_numbers
    
#print(abundant_numbers())
</cell>
<text>
Problem 5
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).