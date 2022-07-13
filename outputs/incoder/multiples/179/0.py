
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 5, 3 or 2 below 600.
    """    
    
    multiples = []
    
    for i in range(1, 600):
        if i % 5 == 0 and i % 3 == 0:
            multiples.append(i)
        elif i % 5 == 0:
            multiples.append(i)
        elif i % 3 == 0:
            multiples.append(i)
            
    return multiples 

#print multiples()
</cell>
<cell>
def primes():
    """
    Generate a list of all the prime numbers less than 600. 
    """
    
    primes = []
    
    for i in range(2, 600):
        is_prime = True
        for n in range(2, i):
            if i % n == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            
    return primes

#print primes()
</cell>
<cell>
def prime_factors(n):
    """
    Generate a list of all the prime factors of n. 
    """
    
    factors = []
    
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
            
    return factors

#print prime_factors(600)
</cell>
<cell>
def prime_factors_slow(n):
    """
    Generate a list of all the prime factors of n. 
    """
    
    factors = []
    
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            