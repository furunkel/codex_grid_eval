
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 5 or 3 below 100.
    """    
    
    sum_of_multiples = 0
    
    for num in range(1, 101):
        if num % 5 == 0 or num % 3 == 0:
            sum_of_multiples += num
            
    return sum_of_multiples

print(multiples())
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def sum_of_primes_under_2_million():
    """
    Sum of all primes below 2 million
    """
    
    sum_of_primes = 0
    
    for num in range(2, 2000000):
        if num > 1:
            if num % 2 == 0:
                sum_of_primes += num
            else:
                sum_of_primes += num + 1
                
    return sum_of_primes

print(sum_of_primes_under_2_million())
</cell>
<text>
Problem 8
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


</text>
<cell>
def sum_of_divisors():
    """
    Sum of all divisors
    """
    
    sum_of_divisors = 0
    
    for num in range(1, 1000000):
        if num % 2 == 0:
            sum_of_divisors += num
        else:
            sum_of_divisors += num + 1
            
    return sum_of_divisors

print(sum_of_divisors())
</cell>
<text>
Problem 9
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called am