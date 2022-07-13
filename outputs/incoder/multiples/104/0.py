
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The sum of these multiples is 29.
    Return the sum of all the multiples of 2 or 9 below 200.
    """    
    
    return sum(i for i in range(1, 200) if i % 2 == 0 or i % 9 == 0)
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to sum all the multiples of 2 or 9 below 200.

Now write a generator that produces all the multiples of 7 below 100 (including 100!). Do not use the number 100!


</text>
<cell>
def multiples_7():
    """
    Generate all the multiples of 7 below 100 (including 100!).
    """
    
    return sum(i for i in range(1, 101) if i % 7 == 0)
</cell>
<cell>
multiples_7()
</cell>
<text>
Now write a generator that produces all the numbers of the form 7k+1 where k is from 1 to 6. Use your generator to find the sum of the first 3000 primes.


</text>
<cell>
def sum_of_primes_7k():
    """
    Find the sum of the first 3000 primes.
    """
    
    return sum(i for i in range(1, 301) if i % 7 == 0)
</cell>
<cell>
sum_of_primes_7k()
</cell>
<text>
Now we are ready to get into infinite sequences. Here is a generator that produces the first N Fibonacci numbers:


</text>
<cell>
def fibonacci(N):
    """
    Produce the values of the Fibonacci sequence up to N.
    
    >>> list(fibonacci(10))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    
    a, b = 0, 1
    while a < N:
        yield a
        a, b = b, a + b
</cell>
<cell>
fibonacci(10)
</cell>
<text>
Now write a generator that produces the first N prime numbers.


</text>
<cell>
def prime_numbers(N):
    """
    Produce the values of the prime numbers up to N.
    
    >>> list(prime_numbers(10))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    
    numbers = prime_numbers_up_to_N(N)
    
    return sum(numbers)
</cell>
<cell>
prime_numbers(10)
</cell>
<text>
Now use your generator to calculate the sum of the first 3000 prime numbers.


</text>
<cell>
def sum_of_primes_3000:
    """
    Find the sum of the first 3000 prime numbers.
    """
    
    return sum(prime_numbers(300