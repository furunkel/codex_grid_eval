def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 1.0, 2: 1.414, 3: 1.732}

    """
    d = {}
    for i in range(1, n + 1):
        d[i] = (i - 1) * (i - 1) / (i - 1)
    return d


def generate_list(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    [1, 1.0, 2, 1.414, 3]

    """
    l = []
    for i in range(1, n + 1):
        l.append(i)
    return l


def generate_dict_with_list(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 1.0, 2: 1.414, 3: 1.732}

    """
    d = {}
    for i in range(1, n + 1):
        d[i] = (i - 1) * (i - 1) / (i - 1)
    return d


def generate_list_with_dict(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 1.