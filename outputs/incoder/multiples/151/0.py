
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 5, we get 2, 4, 5, 6, 8, 10, 12 and 14. The product of these multiples is 3225600.
    Return the product of all the multiples of 2 or 5 below 600.
    """    
    
    multiples = []
    
    for n in range(15):
        if n % 2 == 0 or n % 5 == 0:
            multiples.append(n)
            
    return multiples 
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to find the products of all the multiples of 2 below a certain number, and all the multiples of 5 below a certain number.

Problem Problem 1
Using what you learned about lists, write a function that computes the factorial of a number. For example, factorial(5) = n!


</text>
<cell>
def factorial(n):
    """
    Compute factorial of n
    """
    
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i
        
    return factorial
</cell>
<cell>
factorial(5)
</cell>
<text>
Great! Your factorial function works perfectly:


</text>
<cell>
factorial(10)
</cell>
<text>
Problem 2
Using what you learned about lists, write a function that computes the factorial of a number. For example, factorial(5) = n!


</text>
<cell>
def factorial(n):
    """
    Compute factorial of n
    """
    
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i
        
    return factorial
</cell>
<cell>
factorial(5)
</cell>
<text>
Problem 3
Write a function that converts a hexadecimal number to its integer representation. For example, 72 = 7$_2$ and F = 15$_x$


</text>
<cell>
def hex_to_int(hex_string):
    """
    Converts a hexadecimal string to its integer representation
    """
    
    hex_int = int(hex_string, 16)
    
    return hex_int
</cell>
<cell>
hex_to_int('7')
</cell>
<cell>
hex_to_int('15')
</cell>
<text>
Problem 4
Write a function that takes in a list of digits, and returns the number of digits that are 1's. You may assume that the given digits are a list of integers representing digits of a hexadecimal number.


</text>
<cell>
def count_ones(digits):
    """
    Counts the number of 1's in a hexadecimal number
    """
    
    count = 0
    
    for digit in digits:
        if digit == 1:
            count += 1
            
    return count
</cell>
<cell>
count_ones([1, 1, 0, 1])
</cell>
<text>
Problem 5
