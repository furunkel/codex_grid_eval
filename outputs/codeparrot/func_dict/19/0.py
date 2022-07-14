def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 1.0}

    """
    d = {}
    for i in range(1, n + 1):
        d[i] = 1.0 / sqrt(i)
    return d


def generate_list(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    [1, sqrt(i)]

    """
    return [i for i in range(1, n + 1)]


def generate_dict_with_limits(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 1.0, sqrt(i): 1.0}

    """
    d = {}
    for i in range(1, n + 1):
        d[i] = 1.0 / sqrt(i)
    return d


def generate_list_with_limits(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    [1, sqrt(i)]

    """
    return [i for i in range(1, n + 1)]


def generate_dict_with_limits_with_limits(n):
    """
    With a given integral number n, write a program to generate a dictionary