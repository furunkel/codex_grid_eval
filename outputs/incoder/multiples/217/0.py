
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 9, we get 2, 4, 6, 8, 9, 10, 12 and 14. The product of these multiples is 5806080.
    Return the product of all the multiples of 2 or 9 below 200.
    """    
    
    multiples = []
    
    for n in range(2, 200):
        if n % 2 == 0:
            if n % 9 == 0:
                multiples.append(n)
            else:
                multiples.append(n * 9)
        else:
            multiples.append(n * 2)
            
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
The square of the sum of the primes below 10 is 2 + 4 + 9 + 16 = 78.
Find the sum of all the primes below 1000 that are perfect squares.


</text>
<cell>
def prime_sum(n):
    """
    Calculates the sum of all primes below n.
    """
    
    primes = []
    
    for n in range(2, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(3, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(5, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(7, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(11, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(13, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(17, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    return sum(primes)
</cell>
<cell>
prime_sum(1000)
</cell>
<cell>
def prime_sum(n):
    """
    Calculates the sum of all primes below n.
    """
    
    primes = []
    
    for n in range(2, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(3, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(5, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(7, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(11, n):
        if n % 2 == 0:
            primes.append(2)
        else:
            primes.append(3)
            
    for n in range(13, n):
        if n % 2 == 0:
            primes.append(2)
        else: