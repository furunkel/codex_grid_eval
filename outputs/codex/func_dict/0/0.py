
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    d = {}
    for i in range(1, n + 1):
        d[i] = i + i
    return d


def generate_dict_comprehension(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return {i: i + i for i in range(1, n + 1)}


def generate_dict_lambda(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return dict(map(lambda i: (i, i + i), range(1, n + 1)))


def generate_dict_lambda_comprehension(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return {i: i + i for i in map(lambda i: i, range(1, n + 1))}


def generate_dict_lambda_comprehension_2(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return {i: i + i for i in map(lambda i: i, range(1, n + 1))}


def generate_dict_lambda_comprehension_3(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return {i: i