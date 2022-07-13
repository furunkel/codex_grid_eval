
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 7 or 9, we get 5, 7 and 9. The sum of these multiples is 21.
    Return the sum of all the multiples of 5, 7 or 9 below 200.
    """    
    
    return sum(x for x in range(1, 200) if x % 5 == 0 or x % 7 == 0 or x % 9 == 0)
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to sum all the multiples of 3 or 5 below 1000.


</text>
<text>
Problem 2b
Use list comprehension to return the square of all the numbers from 1 to 1000 (both included).


</text>
<cell>
def squares():
    """
    Return the square of all the numbers from 1 to 1000 (both included).
    """
    
    return [i**2 for i in range(1, 1001)]
</cell>
<cell>
squares()
</cell>
<text>
Problem 2c
Use list comprehension to return the square of all the numbers from 1 to 1000 (both included) that are not perfect squares.


</text>
<cell>
def not_perfect_squares():
    """
    Return the square of all the numbers from 1 to 1000 (both included) that are not perfect squares.
    """
    
    return [i**2 for i in range(1, 1001) if not i**2 == i]
</cell>
<cell>
not_perfect_squares()
</cell>
<text>
Problem 2d
Use list comprehension to return the square of all the numbers from 1 to 1000 (both included) that are not perfect squares or are perfect squares.


</text>
<cell>
def not_perfect_squares():
    """
    Return the square of all the numbers from 1 to 1000 (both included) that are not perfect squares or are perfect squares.
    """
    
    return [i**2 for i in range(1, 1001) if not i**2 == i or i**2 == i]
</cell>
<cell>
not_perfect_squares()
</cell>
<text>
Problem 2e
Use list comprehension to generate all the prime numbers less than 1000 (both included).


</text>
<cell>
def primes():
    """
    Generate all the prime numbers less than 1000 (both included).
    """
    
    return [i**2 for i in range(1, 1001) if i**2 != i]
</cell>
<cell>
primes()
</cell>
<text>
Problem 2f
Use list comprehension to generate all the prime numbers less than or equal to 1000 (both included).


</text>
<cell>
def primes():
    """
    Generate all the prime numbers less than or equal to 1000 (both included).
    """
    
    return [i**2 for i in range(1, 1001) if i**2 <= i]
</cell>
<cell>
primes()