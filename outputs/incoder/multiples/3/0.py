
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The product of these multiples is 810.
    Return the product of all the multiples of 3 or 5 below 124.
    """    
    
    multiples = []
    
    for i in range(1, 125):
        if i % 5 == 0 or i % 3 == 0:
            multiples.append(i)
            
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to check if a number is even or odd, and how to sum all the multiples of 3 or 5 below 1000.


</text>
<text>
Problem 9
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def sum_of_primes_under_2million():
    """
    Sum of all the primes below 2 million
    """
    
    primes = []
    
    for i in range(2, 2000000):
        if isprime(i):
            primes.append(i)
            
    return sum(primes)
</cell>
<cell>
sum_of_primes_under_2million()
</cell>
<text>
Great! Now you know how to find the sum of all the primes below two million, and how to check if a number is prime or not.


</text>
<text>
Problem 10
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


</text>
<cell>
def sum_of_amicable_numbers():
    """
    Sum of all the amicable numbers under 10000
    """
    
    amicable_numbers = []
    
    for i in range(1, 10000):
        if isprime(i) and amicable(i):
            amicable_numbers.append(i)
            
    return sum(amicable_numbers)
</cell>
<cell>
sum_of_amicable_numbers()
</cell>
<text>
Great! Now you know how to find the sum of all the amicable numbers under 10000.


</text>
<text>
Problem 11
Let us list all the natural numbers below 10 that are multiples of 3 or 5, but not 9, because 9 can be divided by 3 but not 5.

73, 79, and 81 are amicable numbers.
Find the sum of all the amicable numbers 