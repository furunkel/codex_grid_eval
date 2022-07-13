
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The product of these multiples is 8.
    Return the product of all the multiples of 2 or 5 below 1000.
    """    
    return sum([i for i in range(1, 1000) if i % 2 == 0 or i % 5 == 0])

# <codecell>

def primes():
    """
    We list all the natural numbers below 10 that are primes. 
    
    Return the sum of all the primes below 1000.
    """
    return sum([i for i in range(1, 1000) if isprime(i)])

# <codecell>

def primes_less_than(n):
    """
    We list all the natural numbers below n that are primes. 
    
    Return the sum of all the primes below n.
    """
    return sum([i for i in range(1, n) if isprime(i)])

# <codecell>

def primes_less_than_or_equal_to(n):
    """
    We list all the natural numbers below n that are primes. 
    
    Return the sum of all the primes below or equal to n.
    """
    return sum([i for i in range(1, n) if isprime(i) or i == n])

# <codecell>

def primes_greater_than(n):
    """
    We list all the natural numbers above n that are primes. 
    
    Return the sum of all the primes above n.
    """
    return sum([i for i in range(n, 1000) if isprime(i)])

# <codecell>

def primes_greater_than_or_equal_to(n):
    """
    We list all the natural numbers above n that are primes. 
    
    Return the sum of all the primes above or equal to n.
    """
    return sum([i for i in range(n, 1000) if isprime(i) or i == n])

# <codecell>

def primes_less_than_or_equal_to_or_equal_to(n):
    """
    We list all the natural numbers below n that are primes. 
    
    Return the sum of all the primes below or equal to or equal to n.
    """
    return sum([i for i in range(n, 1000) if isprime(i) or i == n])

# <codecell>

def primes_greater_than_or_equal_to_or_equal_to(n):
    """
    We list all the natural numbers above n that are primes. 
    
    Return the sum of all the primes above or equal to or equal to n.
    """
    return sum([i for i in range(n, 1000) if isprime(i) or i == n])

# <codecell>

def primes_less_than_or_equal_to_or_equal_to_or_equal_to(n):
    """
    We list all the natural numbers below n that are primes. 
    
    Return the sum of all the primes below or equal to or equal to n.
    """
    return sum([i for i in range(n, 1000) if isprime(i) or i == n])

# <codecell>

def primes_greater_