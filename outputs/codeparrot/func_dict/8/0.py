
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 0, 2: 0, 3: 0}

    """
#    n = int(n)
    if n == 0:
        return {}
    else:
        return generate_dict(n-1)

def generate_list(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    [1, 2, 3]

    """
#    n = int(n)
    if n == 0:
        return []
    else:
        return generate_list(n-1)

def generate_dict_of_lists(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: [1, 2, 3], 2: [1, 2, 3]}

    """
#    n = int(n)
    if n == 0:
        return {}
    else:
        return generate_dict_of_lists(n-1)

def generate_list_of_dicts(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: [1, 2, 3], 2: [1, 2, 3]}

    """
#    n = int(n)
   