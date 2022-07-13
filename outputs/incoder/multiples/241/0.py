
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5 or 3, we get  and 3. The product of these multiples is 3.
    Return the product of all the multiples of 5 or 3 below 124.
    """    
    
    multiples = []
    
    for n in range(124,0,-1):
        if n % 5 == 0 or n % 3 == 0:
            multiples.append(n)
            
    return multiples 
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to get the multiples of 5 below 1000.


</text>
<text>
Problem 7
Write a function that computes the factorial of a number. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120


</text>
<cell>
def factorial(n):
    """
    Compute the factorial of n!
    """
    
    factorial = 1
    
    for i in range(1,n+1):
        factorial *= i
        
    return factorial
</cell>
<cell>
factorial(5)
</cell>
<text>
Problem 8
Write a function that converts a decimal to a binary string, and returns the string with “0b” prefix. For example, decimal_to_binary3(12) = "0b1100".


</text>
<cell>
def decimal_to_binary(n):
    """
    Convert n to a binary string.
    """
    
    binary = bin(n).replace("0b","")
    
    return binary
</cell>
<cell>
decimal_to_binary(12)
</cell>
<text>
Problem 9
Write a function that checks whether a passed string is palindrome or not.


</text>
<cell>
def palindrome(s):
    """
    Checks whether a string is a palindrome or not.
    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
