
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5 or 3, we get  and 3. The sum of these multiples is 3.
    Return the sum of all the multiples of 5 or 3 below 124.
    """    
    
    sum = 0
    for i in range(1, 125):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def sum_of_primes_below(n):
    """
    Sum of all primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
    return sum
</cell>
<cell>
sum_of_primes_below(2000000)
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the sum of the first six prime numbers is 23.

What is the sum of the numbers on the left of the colon in this figure?


</text>
<text>
None 



</text>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a nested for loop to sum all the primes below two million.


</text>
<cell>
def sum_of_primes_below(n):
    """
    Sum of all primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
            for j in range(2, i):
                if isprime(j):
                    sum += j
    return sum
</cell>
<cell>
sum_of_primes_below(2000000)
</cell>
<text>
Problem 11
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a nested for loop to sum all the primes below two million.


</text>
<cell>
def sum_of_primes_below(n):
    """
    Sum of all primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if isprime(i):
            sum += i
            for j in range(2, i):
                if isprime(j):
                    sum += j
    return sum
</cell>
<cell>
sum_of_primes_below(2000000)
</cell>
<text>
Problem 12
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the sum of the first six prime numbers is 23.

Find the sum of all the primes below two milli