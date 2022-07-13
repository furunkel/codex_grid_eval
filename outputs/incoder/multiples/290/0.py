
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5, 3 or 2, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 5, 3 or 2 below 600.
    """    
    
    sum = 0
    for i in range(1, 600):
        if i % 5 == 0 or i % 3 == 0 or i % 2 == 0:
            sum += i
    return sum

# print multiples()
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
# Problem 8

def prime_sum():
    """
    Find the sum of all the primes below two million.
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

# print prime_sum()
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers on the left of the middle five prime numbers?


</text>
<cell>
# Problem 9

def sum_of_left_five_primes():
    """
    Find the sum of the numbers on the left of the middle five prime numbers.
    """
    
    sum = 0
    for i in range(2, 6):
        if isprime(i):
            sum += i
    return sum

# print sum_of_left_five_primes()
</cell>
<text>
Problem 10
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Hint: consider the terms in the Fibonacci sequence whose values do not exceed four million.

$Fn = F{n-1} + F_{n-2}$

$F{n-1} = 1$

$F_{n-2} = 1$

$Fn = F{n-1} + F_{n-2}$

$F{n-1} = 2$

$F_{n-2} = 3$

$Fn = F{n-1} + F_{n-2}$

$F{n-1} = 5$

$F_{n-2} = 8$

$Fn = F{n-1} + F_{n-2}$

$F{n-1} = 13$

$F_{n-2} = 21$

$Fn = F{n-1} + F_{n-2}$

$F{n-1} = 55$

$F_{n-2} = 89$

$Fn = F{n-1} + F_{n-2}$

$F{n-1} = 144$

$F_{n-2} = 233$

$Fn = F