
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i**2) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    """
    
    dictionary = {}
    
    for i in range(1, n+1):
        dictionary[i] = i**2
        
    return dictionary
</cell>
<cell>
# test your code
assert generate_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
</cell>
<text>
Write a Python program to generate a dictionary that contains (i, i**2) such that i is a non-negative integer less than or equal to 10 (both included) and then the program should return the dictionary.

</text>
<cell>
def generate_dict_2(n):
    """
    With a given non-negative integer n, write a program to generate a dictionary that contains (i, i**2) such that
    i is a non-negative integer less than or equal to 10 (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    10
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

    """
    
    dictionary = {}
    
    for i in range(1, n+1):
        dictionary[i] = i**2
        
    return dictionary
</cell>
<cell>
# test your code
assert generate_dict_2(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
</cell>
<text>
Write a Python program to generate a dictionary that contains (i, i**2) such that i is a non-negative integer less than or equal to 100 (both included) and then the program should return the dictionary.

</text>
<cell>
def generate_dict_3(n):
    """
    With a given non-negative integer n, write a program to generate a dictionary that contains (i, i**2) such that
    i is a non-negative integer less than or equal to 100 (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    100
    Then, the output should be:
    {1: 1, 2: 9, 3: 81, 4: 64, 5: 49, 6: 36, 7: 25, 8: 16, 9: 9, 10: 1}

    """
    
    dictionary = {}
    
    for i in range(1, n+1):
        dictionary[i] = i**2
        
    return dictionary
</cell>
<cell>
# test your code
assert generate_dict_3(100) == {1: 1, 2: 9, 3: 81, 4: 64, 5: 49, 6: 36, 7: 25, 8: 16, 9: 9, 10: 1}
</cell>
<text>
Write a Python program to generate a dictionary that contains (i, i**2) such that i is a non-negative integer 