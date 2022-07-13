
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 2, 3 or 5 below 200.
    """    
    
    sum = 0
    
    for i in range(1, 201):
        if i % 2 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
            
    return sum

# print multiples()
</cell>
<text>
Problem 3
Use while True loop to find the sum of all the natural numbers below 10 that are multiples of 3 or 5.


</text>
<cell>
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 2, 3 or 5 below 200.
    """    
    
    sum = 0
    
    for i in range(1, 201):
        if i % 2 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
            
    return sum

# print multiples()
</cell>
<text>
Problem 4
Write a Python program to find the largest prime factor of the number 600851475143. 
The largest prime factor is 7919
The below program should return 7919


</text>
<cell>
def prime_factors(n):
    """
    Find the prime factors of a given natural number.
    """
    
    factors = []
    
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
            
    return factors

# print prime_factors(600851475143)
</cell>
<text>
Problem 5
Write a Python program to check whether a given number is prime or not. 
A number is prime if it has only two distinct prime factors, namely 1 and itself. 
For example, 6 is prime because 6 = 2 * 1.


</text>
<cell>
def prime_check(n):
    """
    Check whether a number is prime or not.
    """
    
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# print prime_check(6)
</cell>
<text>
Problem 6
Write a Python program to check whether a given number is palindrome or not.
A palindrome is a word, number, or other sequence of characters which reads the same backward as forward.
For example, 1221 is a palindrome.


</text>
<cell>
def palindrome_check(n):
    """
    Check whether a number is palindrome or not.
    """
    
    return n == n[::-1]

# print palindrome_check(1221)
</cell>
<text>
Problem 7
Write a Python program to check whether a given number is 