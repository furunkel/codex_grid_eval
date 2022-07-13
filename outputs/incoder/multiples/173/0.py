
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 5, 3 or 2 below 197.
    """    
    
    multiples = []
    
    for n in range(2, int(math.sqrt(197))+1):
        if n % 5 == 0 and n % 3 == 0 and n % 2 == 0:
            multiples.append(n)
            
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Problem 9
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_below_2million():
    """
    Sum of primes below 2 million
    """
    
    primes = []
    
    for n in range(2, int(math.sqrt(2000000))+1):
        if all(n % p != 0 for p in range(2, n)):
            primes.append(n)
            
    return sum(primes)
</cell>
<cell>
primes_below_2million()
</cell>
<text>
Problem 10
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


</text>
<cell>
def sum_of_abundant_numbers():
    """
    Sum of abundant numbers
    """
    
    abundants = []
    
    for n in range(1, int(math.sqrt(28123))+1):
        if all(n % p != 0 for p in range(2, n)):
            abundants.append(n)
            
    return sum(abundants)
</cell>
<cell>
sum_of_abundant_numbers()
</cell>
<text>
Problem 11
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable 