
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5 or 3, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 5 or 3 below 200.
    """    
    
    sum = 0
    for i in range(1, 200):
        if i % 5 == 0 or i % 3 == 0:
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
def primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum

print(primes_below(2000000))
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the sum of the numbers on the left of the middle five prime numbers?


</text>
<cell>
def sum_of_left_five_primes(n):
    """
    Find the sum of all the numbers below n that are on the left of the middle five prime numbers.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            if i % 5 == 0:
                sum += i
    return sum

print(sum_of_left_five_primes(2000000))
</cell>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Can you do it in less than a second?


</text>
<cell>
def primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum

print(primes_below(2000000))
</cell>
<text>
Problem 11
The sum of the first ten natural numbers is,
1! + 2! + 3! + 4! + 5! + 6! + 7! + 8! + 9! + 10!

The sum of the first ten odd numbers is,
1! + 2! + 3! + 4! + 5! + 6! + 7! + 8! + 9! + 10!

Hence the difference between the sum of the first ten natural numbers and the sum of the first ten odd numbers is 10.

Find the difference between the sum of the first ten natural numbers and the sum of the first ten odd numbers.


</text>
<cell>
def sum_of_first_ten_numbers(n):
    """
    Find the sum of all the numbers below n that are on the 