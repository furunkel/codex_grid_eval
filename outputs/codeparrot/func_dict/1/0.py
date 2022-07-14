def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 2}

    """
    return {i: i + n for i in range(1, n + 1)}


def generate_list(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    """
    return [i for i in range(1, n + 1)]


def generate_dict_with_list(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 2, 3: 4, 5: 6, 7: 8, 9: 9}

    """
    return {i: i + n for i in range(1, n + 1)}


def generate_list_with_dict(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 2, 3: 4, 5: 6, 7: 8, 9: 9}

    """
    return [i for i in range(1, n + 1)]


def generate_dict_with_list_with_dict(n):
    """
    With a given integral number n, write a program to generate