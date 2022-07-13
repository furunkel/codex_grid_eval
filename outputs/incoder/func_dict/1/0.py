
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 2}

    """
    
    dict = {}
    for i in range(1, n + 1):
        dict[i] = i + i
    return dict
</cell>
<cell>
# test your code
d = generate_dict(10)
assert d == {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
</cell>
<text>
Write a Python program to generate a dictionary that contains (i, i**2) such that
i is a integral number between 1 and n (both included) and then the program should return the dictionary.
(Hint: Use a dictionary comprehension.)


</text>
<cell>
def generate_dict_2(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i**2) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 2}

    """
    
    dict = {}
    for i in range(1, n + 1):
        dict[i] = i ** 2
    return dict
</cell>
<cell>
# test your code
d = generate_dict_2(10)
assert d == {1: 4, 2: 9, 3: 16, 4: 25, 5: 36, 6: 49, 7: 64, 8: 81, 9: 100}
</cell>
<text>
Write a Python program to generate a dictionary that contains (i, i**0.5) such that
i is a integral number between 1 and n (both included) and then the program should return the dictionary.
(Hint: Use a dictionary comprehension.)


</text>
<cell>
def generate_dict_3(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i**0.5) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 2}

    """
    
    dict = {}
    for i in range(1, n + 1):
        dict[i] = i ** 0.5
    return dict
</cell>
<cell>
# test your code
d = generate_dict_3(10)
assert d == {1: 1, 2: 1.5, 3: 2.25, 4: 2.8333333333333335, 5: 3.625, 6: 4.5, 7: 5.166666666666667, 8: 5.8333333333333334, 9: 6.5833333333333334}
</cell>
<text>
Write a Python program to generate a dictionary that contains (i, i**2) such that
i is a integral number between 1 and n (both included) and then the program 