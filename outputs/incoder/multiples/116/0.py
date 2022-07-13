
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 3 or 5 below 197.
    """    
    
    sum = 0
    for i in range(1, 201):
        if i % 5 == 0 or i % 3 == 0:
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
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(sum(primes_below(2000000)))
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers in the first ten thousand primes?


</text>
<cell>
def sum_of_primes(n):
    """
    Sum the first n primes.
    """
    
    sum = 0
    for i in range(2, n):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            sum += i
    return sum

print(sum_of_primes(10000))
</cell>
<text>
Problem 9
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


</text>
<cell>
def sum_of_evens(n):
    """
    Sum the even-valued terms in the Fibonacci sequence.
    """
    
    sum = 0
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        if a % 2 == 0:
            sum += a
    return sum

print(sum_of_evens(4000000))
</cell>
<text>
Problem 10
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def largest_palindrome(n):
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    
    largest = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j == i * str(j)[::-1]:
                if i * j > largest:
                    largest = i * j
