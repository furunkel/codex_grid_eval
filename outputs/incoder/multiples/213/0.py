
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 9, we get 2, 4, 6, 8, 9, 10, 12 and 14. The product of these multiples is 5806080.
    Return the product of all the multiples of 2 or 9 below 124.
    """    
    
    multiples = []
    
    for i in range(1, 15):
        if i % 2 == 0 or i % 9 == 0:
            multiples.append(i)
            
    return multiples[len(multiples) - 1]
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
    Sum of all primes below n
    """
    
    primes = []
    
    for i in range(2, n):
        if i not in primes:
            primes.append(i)
            
    return sum(primes)
</cell>
<cell>
sum_of_primes(2000000)
</cell>
<text>
Problem 8
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


</text>
<cell>
def sum_of_divisors(n):
    """
    Sum of all divisors below n
    """
    
    divisors = []
    
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
            
    return sum(divisors)
</cell>
<cell>
sum_of_divisors(28123)
</cell>
<text>
Problem 9
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 