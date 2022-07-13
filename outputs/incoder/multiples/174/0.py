
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 5, 3 or 2 below 200.
    """    
    
    sum = 0
    for i in range(1, 200):
        if i % 5 == 0 and i % 3 == 0 or i % 2 == 0:
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
def sum_of_primes_under_2_million():
    """
    Find the sum of all the primes below two million.
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(sum_of_primes_under_2_million())
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers in the first six prime numbers?


</text>
<cell>
def sum_of_prime_numbers_under_six():
    """
    Find the sum of all the prime numbers below six.
    """
    
    sum = 0
    for i in range(2, 6):
        if isprime(i):
            sum += i
    return sum

print(sum_of_prime_numbers_under_six())
</cell>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers: 2, 3, 5, 7, 11, and 13.


</text>
<cell>
def sum_of_first_six_prime_numbers():
    """
    Find the sum of the first six prime numbers.
    """
    
    sum = 0
    for i in range(2, 6):
        if isprime(i):
            sum += i
    return sum

print(sum_of_first_six_prime_numbers())
</cell>
<text>
Problem 11
The sum of the first ten natural numbers is: $1! + 2! + 3! + 4! + 5! + 6! + 7! + 8! + 9! + 10! = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55$.

Find the sum of all the first ten natural numbers.


</text>
<cell>
def sum_of_first_ten_numbers():
    """
    Find the sum of the first ten natural numbers.
    """
    
    sum = 0
    for i in range(1, 11):
        sum += i
    return sum

print(sum_of_first_ten_numbers())
</cell>
<text>
Problem 12
By listing the first six prime numbers: 2, 3, 5, 7, 11, 