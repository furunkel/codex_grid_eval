
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 9, we get 2 and 4. The sum of these multiples is 6.
    Return the sum of all the multiples of 2 or 9 below 197.
    """    
    sum = 0
    for i in range(1, 20):
        if i % 2 == 0:
            sum += i
        elif i % 9 == 0:
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
def primes_sum():
    """
    Sum of all primes below two million
    """
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(primes_sum())
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers on the left of the middle five prime numbers? That is, what is 13?

NOTE: 2, 3, 5, 7, 11, and 13 are not included in the sum.


</text>
<cell>
def sum_of_left_five_primes():
    """
    Sum of all numbers below two million
    """
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(sum_of_left_five_primes())
</cell>
<text>
Problem 9
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

The Fibonacci sequence is defined by the recurrence relation:

Fn = F(n-1) + F(n-2) for n > 1.


where F(0) = 0, F(1) = 1 and F(n) = F(n - 1) + F(n - 2) for n > 1.


For example, F(10) = 55 and F(9) = 89.

What is the sum of the even Fibonacci numbers below two million?


</text>
<cell>
def sum_of_even_fibonacci_numbers():
    """
    Sum of even Fibonacci numbers below two million
    """
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
            if i % 2 == 0:
                sum += i
    return sum

print(sum_of_even_fibonacci_numbers())
</cell>
<text>
Problem 10
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the odd-valued terms.

The Fibonacci sequence is defined by the recurrence relation:

Fn = F(n-1