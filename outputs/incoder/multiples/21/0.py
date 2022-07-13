
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5 or 3, we get 3, 5, 6 and 9. The product of these multiples is 810.
    Return the product of all the multiples of 5 or 3 below 200.
    """    
    
    multiples = []
    
    for n in range(1, 201):
        if n % 5 == 0 or n % 3 == 0:
            multiples.append(n)
            
    return sum(multiples)

print(multiples())
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for n in range(2, n):
        is_prime = True
        for p in range(2, n):
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            
    return primes

print(sum(primes_below(2000000)))
</cell>
<text>
Problem 9
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def sum_of_divisors(n):
    """
    Sum of divisors of a number.
    """
    
    sum = 0
    
    for divisor in range(1, n):
        if n % divisor == 0:
            sum += divisor
            
    return sum

print(sum_of_divisors(28123))
</cell>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for n in range(2, n):
        is_prime = True
        for p in range(2, n):
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            
    return primes

print(sum(primes_below(2