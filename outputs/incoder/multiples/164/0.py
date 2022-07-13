
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 2, 3 or 5 below 600.
    """    
    
    sum = 0
    for i in range(1, 600):
        if i % 2 == 0:
            if i % 3 == 0:
                if i % 5 == 0:
                    sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_under_2million():
    """
    Find the sum of all the primes below two million.
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(primes_under_2million())
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers on the left of the middle five prime numbers?


</text>
<cell>
def sum_of_left_five_primes():
    """
    Find the sum of all the numbers on the left of the middle five prime numbers.
    """
    
    sum = 0
    for i in range(2, 6):
        if isprime(i):
            sum += i
    return sum

print(sum_of_left_five_primes())
</cell>
<text>
Problem 10
Let us list all the natural numbers below 10 that are multiples of 3 or 5, but not both. Then, find the sum of the numbers. What is the sum of all the numbers?


</text>
<cell>
def sum_of_multiples():
    """
    Find the sum of all the numbers that are multiples of 3 or 5, but not both.
    """
    
    sum = 0
    for i in range(1, 11):
        if isprime(i) and i % 3 != 0 and i % 5 != 0:
            sum += i
    return sum

print(sum_of_multiples())
</cell>
<text>
Problem 11
Let us list all the natural numbers below 10 that are multiples of 3 or 5, but not both. Then, find the sum of the numbers. What is the sum of all the numbers that are multiples of 3 or 5, but not both?


</text>
<cell>
def sum_of_multiples():
    """
    Find the sum of all the numbers that are multiples of 3 or 5, but not both.
    """
    
    sum = 0
    for i in range(1, 11):
        if isprime(i) and i % 3 != 0 and i % 5 != 0:
            sum += i
    return sum

print(sum_of_multiples())
</cell>
<text>
Problem 12
Let us list all the natural numbers below 10 that are multiples of 3 or 5, but not both. Then, find the sum of the 