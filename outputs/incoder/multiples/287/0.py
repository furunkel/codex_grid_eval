
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5, 3 or 2, we get 2, 3 and 4. The product of these multiples is 24.
    Return the product of all the multiples of 5, 3 or 2 below 200.
    """    
    return sum([x for x in xrange(5, 200) if x % 5 == 0 or x % 3 == 0])

def primes():
    """
    Generate a list of all the prime numbers less than 200.
    """
    primes = []
    for x in xrange(2, 200):
        if all(x % p != 0 for p in primes):
            primes.append(x)
    return primes

def primes_upto(limit):
    """
    Generate a list of all the prime numbers less than or equal to limit.
    """
    primes = []
    for x in xrange(2, limit):
        if all(x % p != 0 for p in primes):
            primes.append(x)
    return primes

def primes_upto_limit(limit):
    """
    Generate a list of all the prime numbers less than or equal to limit.
    """
    primes = []
    for x in xrange(2, limit):
        if all(x % p != 0 for p in primes):
            primes.append(x)
    return primes

def primes_upto_limit_with_prime_divisors(limit):
    """
    Generate a list of all the prime numbers less than or equal to limit.
    """
    primes = []
    for x in xrange(2, limit):
        if all(x % p != 0 for p in primes):
            primes.append(x)
            
    prime_divisors = []
    for p in primes:
        for d in xrange(2, p):
            if p % d == 0:
                prime_divisors.append(d)
                break
    return primes

def primes_upto_limit_with_prime_divisors_2(limit):
    """
    Generate a list of all the prime numbers less than or equal to limit.
    """
    primes = []
    for x in xrange(2, limit):
        if all(x % p != 0 for p in primes):
            primes.append(x)
            
    prime_divisors = []
    for p in primes:
        for d in xrange(2, p):
            if p % d == 0:
                prime_divisors.append(d)
                break
    return primes

def primes_upto_limit_with_prime_divisors_3(limit):
    """
    Generate a list of all the prime numbers less than or equal to limit.
    """
    primes = []
    for x in xrange(2, limit):
        if all(x % p != 0 for p in primes):
            primes.append(x)
            
    prime_divisors = []
    for p in primes:
        for d in xrange(2, p):
            if p % d == 0:
                prime_divisors.append(d)
                break
    return primes

def primes_upto_limit_with_prime_divisors_4(limit):
    """
    Generate a list of all the prime numbers less than or equal to limit.
    """
    primes = []
    for x in xrange(2, limit):
        if all(x % p 