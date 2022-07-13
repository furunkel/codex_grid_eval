
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 9, we get 2, 4, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 65.
    Return the sum of all the multiples of 2 or 9 below 124.
    """    
    sum = 0
    for i in range(1, 125):
        if i % 2 == 0:
            sum += i
        if i % 9 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def prime_sum():
    """
    Find the sum of all the primes below two million.
    """
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(prime_sum())
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the sum of the first six prime numbers is 23.

What is the sum of the numbers on the left of the colon in this expression below?

a) $1 + 2 + 3 + 5 + 7 + 11 + 13$

b) $1 + 2 + 3 + 5 + 11 + 13$

c) $1 + 2 + 3 + 5 + 7 + 11 + 13$

d) $1 + 2 + 3 + 5 + 7 + 11 + 13$

e) $1 + 2 + 3 + 5 + 7 + 11 + 13$


</text>
<cell>
def sum_of_primes():
    """
    Find the sum of all the primes below two million.
    """
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(sum_of_primes())
</cell>
<text>
Problem 9
By using the rules of prime numbers, we can find the sum of the primes below two million. Find the sum of all the primes below two million.

None 



</text>
<cell>
def sum_of_primes():
    """
    Find the sum of all the primes below two million.
    """
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(sum_of_primes())
</cell>
<text>
Problem 10
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def largest_palindrome():
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    largest = 0
    for i in range(1, 1000000):
        for j in range(1, 1000000):
            if str(i) * str(