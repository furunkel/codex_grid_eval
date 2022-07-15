
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        dictionary[i] = i - i
        
    return dictionary
</cell>
<cell>
# test your code
print(generate_dict(5))
</cell>
<text>
Write a Python program to generate a dictionary that contains (i, i + 1) such that
i is a integral number between 1 and n (both included) and then the program should return the dictionary.

</text>
<cell>
def generate_dict_2(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + 1) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}

    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        dictionary[i] = i + i
        
    return dictionary
</cell>
<cell>
# test your code
print(generate_dict_2(5))
</cell>
<text>
Write a Python program to generate a dictionary that contains (i, i - 1) such that
i is a integral number between 1 and n (both included) and then the program should return the dictionary.

</text>
<cell>
def generate_dict_3(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i - 1) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        dictionary[i] = i - 1
        
    return dictionary
</cell>
<cell>
# test your code
print(generate_dict_3(5))
</cell>
<text>
Write a Python program to generate a dictionary that contains (i, i + 2) such that
i is a integral number between 1 and n (both included) and then the program should return the dictionary.

</text>
<cell>
def generate_dict_4(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + 2) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2}

    """
