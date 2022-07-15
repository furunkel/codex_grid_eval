
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        dictionary[i] = i + i
    
    return dictionary

print(generate_dict(5))
</cell>
<text>
Problem 3
Write a Python program to generate a dictionary that contains (i, i + 1) such that
i is a integral number between 1 and n (both included) and then the program should return the dictionary.

Suppose the following input is supplied to the function:
5
Then, the output should be:
{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

</text>
<cell>
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + 1) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        dictionary[i] = i + i
    
    return dictionary

print(generate_dict(5))
</cell>
<text>
Problem 4
Write a Python program to generate a dictionary that contains (i, i + 2) such that
i is a integral number between 1 and n (both included) and then the program should return the dictionary.

Suppose the following input is supplied to the function:
5
Then, the output should be:
{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

</text>
<cell>
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + 2) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        dictionary[i] = i + i
    
    return dictionary

print(generate_dict(5))
</cell>
<text>
Problem 5
Write a Python program to generate a dictionary that contains (i, i + 3) such that
i is a integral number between 1 and n (both included) and then the program should return the dictionary.

Suppose the following input is supplied to the function:
5
Then, the output should be:
{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

</text>
<cell>
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + 3) such that
    i is a integral number between 1 and 