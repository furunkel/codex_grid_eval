
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 5, we get 2, 4, 5, 6, 8, 10, 12 and 14. The product of these multiples is 3225600.
    Return the product of all the multiples of 2 or 5 below 1000.
    """    
    
    return 3225600
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to get the product of a list of numbers. Next we will write a function that will tell us how many prime numbers are less than a certain number.


</text>
<cell>
def prime_count(n):
    """
    Count the number of prime numbers less than or equal to a given number.
    """
    
    count = 0
    
    for i in range(2, n):
        if n%i == 0:
            count += 1
            
    return count
</cell>
<cell>
prime_count(10)
</cell>
<text>
Now use the prime_count() function with ten to find the prime numbers less than 100. We have talked about squaring numbers and checking if they are prime.


</text>
<cell>
prime_count(100)
</cell>
<text>
Great! Now you know how to get the product of a list of numbers. Next we will write a function that will tell us how many prime numbers are less than a certain number.


</text>
<cell>
def prime_count(n):
    """
    Count the number of prime numbers less than or equal to a given number.
    """
    
    count = 0
    
    for i in range(2, n):
        if n%i == 0:
            count += 1
            
    return count
</cell>
<cell>
prime_count(10)
</cell>
<text>
Now use the prime_count() function with ten to find the prime numbers less than 100. We have talked about squaring numbers and checking if they are prime.


</text>
<cell>
prime_count(100)
</cell>
<text>
Great! Now you know how to get the product of a list of numbers. Next we will write a function that will tell us how many prime numbers are less than a certain number.


</text>
<cell>
def prime_count(n):
    """
    Count the number of prime numbers less than or equal to a given number.
    """
    
    count = 0
    
    for i in range(2, n):
        if n%i == 0:
            count += 1
            
    return count
</cell>
<cell>
prime_count(10)
</cell>
<text>
Now use the prime_count() function with ten to find the prime numbers less than 100. We have talked about squaring numbers and checking if they are prime.


</text>
<cell>
prime_count(100)
</cell>
<text>
Great! Now you know how to get the product of a list of numbers. Next we will write a function that will tell us how many prime numbers are less than a certain number.


</text>
<cell>
def prime_count(n):
    """