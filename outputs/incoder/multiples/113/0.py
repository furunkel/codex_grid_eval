
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 100.
    """    
    
    multiples = []
    
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
            
    return sum(multiples)
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
def sum_of_primes(n):
    """
    Sum of all the primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        if i % 2 == 0:
            continue
        
        for p in range(3, i, 2):
            if i % p == 0:
                break
        else:
            primes.append(i)
            
    return sum(primes)
</cell>
<cell>
sum_of_primes(2000000)
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_number(n):
    """
    Find the 10th prime number.
    """
    
    primes = []
    
    for i in range(2, n):
        if i % 2 == 0:
            continue
        
        for p in range(3, i, 2):
            if i % p == 0:
                break
        else:
            primes.append(i)
            
    return primes[9]
</cell>
<cell>
prime_number(1000000)
</cell>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a nested for loop to check all the primes below two million.


</text>
<cell>
def sum_of_primes(n):
    """
    Sum of all the primes below n.
    """
    
    primes = []
    
    for i in range(2, n):
        if i % 2 == 0:
            continue
        
        for p in range(3, i, 2):
            if i % p == 0:
                break
        else:
            primes.append(i)
            
    return sum(primes)
</cell>
<cell>
sum_of_primes(2000000)
</cell>
<text>
Problem 11
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_number(n):
    """
    Find the 10th prime number.
    """
    
    primes = []
    
