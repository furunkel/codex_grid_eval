def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    """
    d = {}
    for i in range(1, n + 1):
        d[i] = i
    return d


def generate_list(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    """
    l = []
    for i in range(1, n + 1):
        l.append(i)
    return l


def generate_dict_of_lists(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    """
    d = {}
    for i in range(1, n + 1):
        d[i] = i
    return d


def generate_list_of_dicts(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    """
    l = []
    for