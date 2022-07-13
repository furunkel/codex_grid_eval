
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 3 or 5 below 200.
    """    
    
    sum = 0
    for i in range(1, 200):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 4
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def prime_sum():
    """
    Sum of all the primes below two million
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(prime_sum())
</cell>
<text>
Problem 5
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers on the left of the middle five prime numbers? That is, what is 13?

NOTE: 2, 3, 5, 7, 11, and 13 are not included in the sum.

</text>
<cell>
def sum_of_left_five():
    """
    Sum of all the numbers on the left of the middle five prime numbers
    """
    
    sum = 0
    for i in range(2, 6):
        if isprime(i):
            sum += i
    return sum

print(sum_of_left_five())
</cell>
<text>
Problem 6
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


</text>
<cell>
def amicable_sum():
    """
    Sum of all the amicable numbers under 10000
    """
    
    sum = 0
    for i in range(1, 10000):
        if isprime(i) and isprime(amicable_number(i)):
            sum += i
    return sum

print(amicable_sum())
</cell>
<text>
Problem 7
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are 