
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 5, 3 or 2 below 600.
    """    
    
    sum = 0
    
    for i in range(1, 600):
        if i % 5 == 0 or i % 3 == 0 or i % 2 == 0:
            sum += i
            
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Problem 3
Use while True loop to find the sum of all the natural numbers below 10 that are multiples of 3 or 5.


</text>
<cell>
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 6, 9, 12, 15, 18, 21, 24, 27, 30.
    Return the sum of all the multiples of 3 or 5 below 10.
    """    
    
    sum = 0
    
    for i in range(1, 10):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Problem 4
Write a Python program to find the sum of all the even numbers below 10 that are multiples of 3 or 5.


</text>
<cell>
def multiples():
    """
    If we list all the even numbers below 10 that are multiples of 3 or 5, we get 3, 6, 9, 12, 15, 18, 21.
    Return the sum of all the even numbers below 10 that are multiples of 3 or 5 below 10.
    """    
    
    sum = 0
    
    for i in range(1, 10):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Problem 5
Write a Python program to find the sum of all the numbers between 1 and 1000 that are divisible by 3 or 5.


</text>
<cell>
def multiples():
    """
    If we list all the numbers between 1 and 1000 that are divisible by 3 or 5, we get 3, 5, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99.
    Return the sum of all the numbers between 1 and 1000 that are divisible by 3 or 5 below 1000.
    """    
    
    sum = 0
    
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Problem 6
Write a Python program to find the largest prime factor of the number 600851475143 .


</text>
<cell>
def largest_prime_factor():
    """
    If we list all the numbers between 1 and 1000 that are 