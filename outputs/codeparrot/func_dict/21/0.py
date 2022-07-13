
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1.0, 2: 1.414, 3: 1.732, 4: 2.0, 5: 2.236}

    """
#    n = int(n)
    if n < 1:
        return {}
    else:
        return generate_dict(n-1)

def generate_list(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    [1, sqrt(i), 1, sqrt(i), 1, sqrt(i)]

    """
#    n = int(n)
    if n < 1:
        return []
    else:
        return generate_list(n-1)

def generate_dict_of_lists(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1.0, 2: 1.414, 3: 1.732, 4: 2.0, 5: 2.236}

    """
#    n = int(n)
    if n < 1:
        return {}
    else:
        return generate_dict_of_lists(n-1)

def generate_list_of_dicts(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function: