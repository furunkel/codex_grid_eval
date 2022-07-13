
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 2, 3 or 5 below 500.
    """    
    
    multiples = []
    
    for i in range(1, 500):
        if i % 2 == 0:
            if i % 3 == 0:
                if i % 5 == 0:
                    multiples.append(i)
    
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Problem 9
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
The square of the sum of the primes below 10 is 2 + 4 + 9 + 16 = 68.
Find the sum of all the primes below 1000 that are perfect squares.

</text>
<cell>
def prime_sum():
    """
    Find the sum of all the primes below 1000 that are perfect squares.
    """
    
    primes = []
    
    for i in range(1, 1000):
        if isprime(i):
            primes.append(i)
    
    return sum(primes)

def square_of_sum():
    """
    Find the square of the sum of the primes below 1000 that are perfect squares.
    """
    
    primes = []
    
    for i in range(1, 1000):
        if isprime(i):
            primes.append(i)
    
    return sum(primes)**2

def sum_of_primes():
    """
    Find the sum of all the primes below 1000 that are perfect squares.
    """
    
    primes = []
    
    for i in range(1, 1000):
        if isprime(i):
            primes.append(i)
    
    return sum(primes)
</cell>
<cell>
prime_sum()
</cell>
<cell>
square_of_sum()
</cell>
<cell>
sum_of_primes()
</cell>
<text>
Problem 10
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

