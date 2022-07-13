
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 1.0}

    """
    d = dict()
    for i in range(1, n+1):
        d[i] = i**2
    return d

def generate_dict_comprehension(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 1.0}

    """
    return {i: i**2 for i in range(1, n+1)}

def generate_dict_comprehension_2(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 1.0}

    """
    return {i: i**2 for i in range(1, n+1) if i % 2 == 0}

def generate_dict_comprehension_3(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 1.0}

    """
    return {i: i**2 for i in range(1, n+1) if i % 2 == 0}

def generate_dict_comprehension_4(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is