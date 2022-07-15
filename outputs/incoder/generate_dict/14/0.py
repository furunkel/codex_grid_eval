
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 1, 2: 4, 3: 9}

    """
    
    dict = {}
    for i in range(1, n + 1):
        dict[i] = i * i
    return dict
</cell>
<cell>
# test your code
d = generate_dict(10)
assert d == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
</cell>
<text>
Write a Python program to generate a dictionary containing all the positive numbers (not necessarily distinct) between 1 and n. (The keys should be the numbers themselves, and the values should be the frequency of those numbers.)


</text>
<cell>
def generate_dict_1(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 1, 2: 4, 3: 9}

    """
    
    dict = {}
    for i in range(1, n + 1):
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict
</cell>
<cell>
# test your code
d = generate_dict_1(10)
assert d == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
</cell>
<text>
Write a Python program to generate a dictionary containing all the positive numbers (not necessarily distinct) between 1 and n. (The keys should be the numbers themselves, and the values should be the frequency of those numbers.)


</text>
<cell>
def generate_dict_2(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 1, 2: 4, 3: 9}

    """
    
    dict = {}
    for i in range(1, n + 1):
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict
</cell>
<cell>
# test your code
d = generate_dict_2(10)
assert d == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
</cell>
<text>
Write a Python program to generate a dictionary containing all the positive numbers (not necessarily distinct) between 1 and n. (The keys should be the numbers themselves, and the values should be the frequency of 