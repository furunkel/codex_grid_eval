
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The product of these multiples is 3456.
    Return the product of all the multiples of 2 or 9 below 600.
    """    
    
    multiples = []
    
    for i in range(1, 600):
        if i % 2 == 0 or i % 9 == 0:
            multiples.append(i)
            
    return sum(multiples)

# print multiples()
</cell>
<text>
Great! Now you know how to find the sum of all the multiples of 2 or 9 below 1000.


</text>
<text>
Problem 3
Write a function that computes the factorial of a number. Do not use loops here.


</text>
<cell>
def factorial(n):
    """
    Compute the factorial of n, a positive integer.
    """
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)
    
# print factorial(5)
</cell>
<text>
Problem 4
Write a function that converts a decimal number to hexadecimal.


</text>
<cell>
def decimal_to_hexadecimal(decimal):
    """
    Convert a decimal number to hexadecimal.
    """
    
    return hex(decimal)[2:]
    
# print decimal_to_hexadecimal(15)
</cell>
<text>
Problem 5
Write a function that converts a binary number to decimal.


</text>
<cell>
def binary_to_decimal(binary):
    """
    Convert a binary number to decimal.
    """
    
    return int(binary, 2)
    
# print binary_to_decimal('1001')
</cell>
<text>
Problem 6
Write a function that checks if a number is palindrome or not.


</text>
<cell>
def is_palindrome(number):
    """
    Check a number to see if it is palindrome or not.
    """
    
    return number == number[::-1]
    
# print is_palindrome(121)
</cell>
<text>
Problem 7
Write a function that takes a list and returns a new list with unique elements of the first list.


</text>
<cell>
def unique_list(my_list):
    """
    Return a new list with unique elements of the first list.
    """
    
    unique_list = []
    
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
            
    return unique_list
    
# print unique_list([1, 1, 2, 3, 4, 4])
</cell>
<text>
Problem 8
Write a Python function that takes a list and returns a new list with all the elements of the first list that come after it in the list.


</text>
<cell>
def after_element(my_list):
    """
    Return a new list with all the elements of the first list that come after it in the list.
    """
    
    after_element_list = []
    
    for i in my_list:
        if i > my_list