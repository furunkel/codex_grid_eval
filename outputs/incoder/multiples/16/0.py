
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5 or 3, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 5 or 3 below 124.
    """    
    
    sum = 0
    for n in range(124, -1, -1):
        if n % 5 == 0 or n % 3 == 0:
            sum += n
    return sum

print(multiples())
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes():
    """
    Sum of all the primes below two million
    """
    
    sum = 0
    for n in range(2, 2000000):
        if all(n % i for i in range(3, n + 1, 2)):
            sum += n
    return sum

print(primes())
</cell>
<text>
Problem 8
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


</text>
<cell>
def abundants():
    """
    Sum of all the abundant numbers below two million
    """
    
    sum = 0
    for n in range(2, 2000000):
        if sum(i for i in range(3, n + 1, 2)) > n:
            sum += n
    return sum

print(abundants())
</cell>
<text>
Problem 9
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


</text>
<cell>
