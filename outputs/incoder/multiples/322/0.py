
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 9, we get 2 and 4. The sum of these multiples is 6.
    Return the sum of all the multiples of 2 or 9 below 100.
    """    
    
    sum = 0
    for i in range(1, 101):
        if i % 2 == 0:
            sum += i
        elif i % 9 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 8
Write a function that computes the factorial of a number. Do not use recursion.

For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120


</text>
<cell>
def factorial(n):
    """
    Compute factorial
    """
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
</cell>
<text>
Problem 9
Write a function that converts a decimal to a hexadecimal value. I.e., instead of returning 6, your function should return '0xc'.

Use a while loop to keep asking the user for a number until they enter a valid number.


</text>
<cell>
def decimal_to_hexadecimal(decimal):
    """
    Convert decimal to hexadecimal
    """
    
    hexadecimal = ''
    
    while decimal != 0:
        hexadecimal += str(decimal % 16).zfill(2)
        decimal = int(decimal/16)
    return hexadecimal

print(decimal_to_hexadecimal(6))
</cell>
<text>
Problem 10
Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1, 2, 2, 3, 4, 4, 4, 6, 7, 7, 7, 8]

Unique List : [1, 2, 3, 4, 6, 7, 8]

</text>
<cell>
def unique_list(list_to_check):
    """
    Remove duplicates from a list
    """
    
    unique_list = []
    
    for item in list_to_check:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(unique_list([1, 2, 2, 3, 4, 4, 4, 6, 7, 7, 7, 8]))
</cell>
<text>
Problem 11
Write a Python function that checks whether a number is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.


</text>
<cell>
def palindrome(number):
    """
    Checks whether a number is palindrome or not
    """
    
    if number == int(str(number)[::-1]):
        return True
    else:
        return False

print(palindrome(12321))
print(palindrome(12321))
print(palindrome(12321))
print(palindrome(12321))
print(palindrome(12321))
print(palindrome(12321))