
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 1.0}

    """
#    n = int(n)
    if n == 1:
        return {1: 1.0}
    else:
        return {i: sqrt(i)}

def generate_list(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    [1, sqrt(i)]

    """
#    n = int(n)
    if n == 1:
        return [1]
    else:
        return [sqrt(i)]

def generate_tuple(n):
    """
    With a given integral number n, write a program to generate a tuple that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the tuple.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    (1, sqrt(i))

    """
#    n = int(n)
    if n == 1:
        return (1,)
    else:
        return (sqrt(i),)

def generate_dict_of_lists(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 1.0, sqrt(i)}

    """
#    n = int(n)
    if n == 1:
        return {1: 1.0}
    else:
        return {i: sqrt(i)}

def generate_