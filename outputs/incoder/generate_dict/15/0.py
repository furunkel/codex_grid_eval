
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        
        if i in dictionary:
            dictionary[i] = dictionary[i] + i
        else:
            dictionary[i] = i
    
    return dictionary
</cell>
<cell>
# test your code
print(generate_dict(5))
</cell>
<text>
Write a Python program to generate a dictionary that contains n key-value pairs, where the value of each pair is the product of 2 given integers.
Suppose the following input is supplied to the function:
2
3
Then, the output should be:
{1: 2, 2: 6}

</text>
<cell>
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    2
    3
    Then, the output should be:
    {1: 2, 2: 6}

    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        
        if i in dictionary:
            dictionary[i] = dictionary[i] * i
        else:
            dictionary[i] = i
    
    return dictionary
</cell>
<cell>
# test your code
print(generate_dict(2))
print(generate_dict(3))
</cell>
<text>
Write a Python program to generate a dictionary that contains n key-value pairs, where the value of each pair is the sum of 2 given integers.
Suppose the following input is supplied to the function:
2
3
Then, the output should be:
{1: 3, 2: 7}

</text>
<cell>
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    2
    3
    Then, the output should be:
    {1: 3, 2: 7}

    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        
        if i in dictionary:
            dictionary[i] = dictionary[i] + i
        else:
            dictionary[i] = i
    
    return dictionary
</cell>
<cell>
# test your code
print(generate_dict(2))
print(generate_dict(3))
</cell>
<text>
Write a Python program to generate a dictionary that contains n key-value pairs, where the value of each pair is the difference of 2 given integers.
Suppose the following input is supplied to the function:
2
3
Then, the output should be:
{1: 1, 2: 