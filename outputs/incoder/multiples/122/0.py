
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 3 or 5 below 600.
    """    
    
    sum = 0
    for i in range(1, 600):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers():
    """
    Generate a list of all the prime numbers below 600.
    """
    
    primes = []
    
    for i in range(2, 600):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
</cell>
<cell>
prime_numbers()
</cell>
<text>
Problem 9
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers():
    """
    Generate a list of all the prime numbers below 600.
    """
    
    primes = []
    
    for i in range(2, 600):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
</cell>
<cell>
prime_numbers()
</cell>
<text>
Problem 10
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers():
    """
    Generate a list of all the prime numbers below 600.
    """
    
    primes = []
    
    for i in range(2, 600):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
</cell>
<cell>
prime_numbers()
</cell>
<text>
Problem 11
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers():
    """
    Generate a list of all the prime numbers below 600.
    """
    
    primes = []
    
    for i in range(2, 600):
        is_prime = True
        for j in primes:
