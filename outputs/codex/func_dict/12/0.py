
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return {i: i * i for i in range(1, n + 1)}


def generate_dict_2(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return dict([(i, i * i) for i in range(1, n + 1)])


def generate_dict_3(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return dict(zip(range(1, n + 1), [i * i for i in range(1, n + 1)]))


def generate_dict_4(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return dict(map(lambda x: (x, x * x), range(1, n + 1)))


def generate_dict_5(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return dict(map(lambda x: (x, x * x), range(1, n + 1)))


def generate_dict_6(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    return dict(map(lambda x: (x, x * x), range(1, n + 1)))


def generate_dict_7(n):
