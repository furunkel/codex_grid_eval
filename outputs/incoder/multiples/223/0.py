
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 9, we get 2, 4, 6, 8, 9, 10, 12 and 14. The product of these multiples is 5806080.
    Return the product of all the multiples of 2 or 9 below 1000.
    """    
    
    multiples = []
    
    for n in range(2, 1000):
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
Problem 9
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_sum():
    """
    Sum of all the primes below two million.
    """
    
    primes = []
    
    for n in range(2, 2000000):
        if n % 2 == 0:
            if n % 3 == 0:
                if n % 5 == 0:
                    if n % 7 == 0:
                        primes.append(n)
                    else:
                        primes.append(n * 7)
                else:
                    primes.append(n * 3)
            else:
                primes.append(n * 2)
        else:
            primes.append(n)
            
    return sum(primes)
</cell>
<cell>
primes_sum()
</cell>
<text>
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a list comprehension.


</text>
<cell>
def primes_sum():
    """
    Sum of all the primes below two million.
    """
    
    primes = [i for i in range(2, 2000000) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0]
    
    return sum(primes)
</cell>
<cell>
primes_sum()
</cell>
<text>
Problem 11
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a list comprehension.


</text>
<cell>
def primes_sum():
    """
    Sum of all the primes below two million.
    """
    
    primes = [i for i in range(2, 2000000) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0]
    
    return sum(primes)
</cell>
<cell>
primes_sum()
</cell>
<text>
Problem 12
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a list comprehension.


</text>
<cell>
def primes_sum():
    """
    Sum of all the primes below two million.
    """
