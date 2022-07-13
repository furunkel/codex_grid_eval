
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8 and 9. The product of these multiples is 51840.
    Return the product of all the multiples of 2, 3 or 5 below 197.
    """    
    
    multiples = []
    
    for n in range(2, 101):
        if n % 2 == 0:
            if n % 3 == 0:
                if n % 5 == 0:
                    multiples.append(n)
    
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Problem 3
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_sum():
    """
    Sum of all the primes below two million
    """
    
    primes = []
    
    for n in range(2, 2000000):
        if n % 2 == 0:
            if n % 3 == 0:
                if n % 5 == 0:
                    primes.append(n)
    
    return sum(primes)
</cell>
<cell>
primes_sum()
</cell>
<text>
Problem 4
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


</text>
<cell>
def abundant_sum():
    """
    Sum of all the positive integers which cannot be written as the sum of two abundant numbers
    """
    
    abundants = []
    
    for n in range(1, 1000000):
        if sum(divisors(n)) == n:
            abundants.append(n)
    
    return sum(abundants)
</cell>
<cell>
abundant_sum()
</cell>
<text>
Problem 5
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.