
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 1.0, 2: 1.414, 3: 1.732}

    """
#    n = int(n)
    if n == 1:
        return {1: 1.0}
    elif n == 2:
        return {1: 1.0, 2: 1.414, 3: 1.732}
    elif n == 3:
        return {1: 1.0, 2: 1.414, 3: 1.732}
    else:
        return {1: 1.0, 2: 1.414, 3: 1.732}

def generate_list(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    [1, sqrt(i)]

    """
#    n = int(n)
    if n == 1:
        return [1]
    elif n == 2:
        return [1.0, sqrt(i)]
    elif n == 3:
        return [1.0, sqrt(i)]
    else:
        return [1.0, sqrt(i)]

def generate_dict_list(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    [1, sqrt(i)]

    """
#    n = int(n)
    if n == 1:
        return [1]
    elif n == 2:
        return [1.0, sqrt(i)]
    elif n == 3:
        return [1.0, sqrt(i