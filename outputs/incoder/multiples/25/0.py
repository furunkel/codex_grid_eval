
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5 or 3, we get 3, 5, 6 and 9. The product of these multiples is 810.
    Return the product of all the multiples of 5 or 3 below 600.
    """    
    
    multiples = []
    
    for num in range(600):
        if num % 5 == 0 or num % 3 == 0:
            multiples.append(num)
            
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Problem 5
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def sum_primes(n):
    """
    Sum of all the primes below n.
    """
    
    primes = []
    
    for num in range(2, n):
        if num in primes:
            continue
        
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            primes.append(num)
            
    return sum(primes)
</cell>
<cell>
sum_primes(2000000)
</cell>
<text>
Problem 6
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a nested for loop to check all the numbers from 2000000.


</text>
<cell>
def sum_primes(n):
    """
    Sum of all the primes below n.
    """
    
    primes = []
    
    for num in range(2, n):
        if num in primes:
            continue
        
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            primes.append(num)
            
    return sum(primes)
</cell>
<cell>
sum_primes(2000000)
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a nested for loop to check all the numbers from 2000000.


</text>
<cell>
def sum_primes(n):
    """
    Sum of all the primes below n.
    """
    
    primes = []
    
    for num in range(2, n):
        if num in primes:
            continue
        
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            primes.append(num)
            
    return sum(primes)
</cell>
<cell>
sum_primes(2000000)
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Hint: Use a nested for loop to check all the numbers from 2000000