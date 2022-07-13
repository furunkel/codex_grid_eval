
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 1000.
    """    
    
    multiples = []
    
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
            
    return sum(multiples)

print(multiples())
</cell>
<text>
Problem 5
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        if i not in primes:
            primes.append(i)
            
    return primes

print(sum(primes_below(2000000)))
</cell>
<text>
Problem 6
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def sum_of_divisors(n):
    """
    Generate a list of divisors of n.
    """
    
    divisors = []
    
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
            
    return divisors

def abundant_number(n):
    """
    Check if n is abundant.
    """
    
    divisors = sum_of_divisors(n)
    
    if sum(divisors) < n:
        return True
    else:
        return False

print(sum(sum_of_divisors(28123)))
print(sum(sum_of_divisors(28124)))
print(sum(sum_of_divisors(28125)))
print(sum(sum_of_divisors(28126)))
print(sum(sum_of_divisors(28127)))
print(sum(sum_of_divisors(28128)))
print(sum(sum_of_divisors(28129)))
print(sum(sum_of_divisors(28130)))
print(sum(sum_of_divisors(28131)))
print(sum(sum_of_divisors(28132)))
print(sum(sum_