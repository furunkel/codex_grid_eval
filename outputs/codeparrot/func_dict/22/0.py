
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    8
    Then, the output should be:
    {1: 1.0, 2: 1.414, 3: 1.732, 4: 2.0, 5: 2.236, 6: 2.449, 7: 2.646, 8: 2.828}

    """
#    n = int(n)
    if n < 1:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return {1: 1.0}
    elif n == 2:
        return {2: 1.0, 3: 1.414, 4: 1.732, 5: 1.236, 6: 1.449, 7: 1.646, 8: 1.828}
    elif n == 3:
        return {4: 1.0, 5: 1.414, 6: 1.732, 7: 1.236, 8: 1.449, 9: 1.646, 10: 1.828}
    elif n == 4:
        return {5: 1.0, 6: 1.414, 7: 1.732, 8: 1.236, 9: 1.449, 10: 1.646, 11: 1.828}
    elif n == 5:
        return {6: 1.0, 7: 1.414, 8: 1.732, 9: 1.236, 10: 1.449, 11: 1.646, 12: 1.828}
    elif n == 6:
        return {7: 1.0, 8: 1.414, 9: 1.732, 10: 1.236, 11: 1.449, 12: 1.646, 13: 1.828}
    elif n == 7:
        return {8: 1.0, 9: 1.414, 10: 1.732, 11: 1.236, 12: 1.449, 13: 1.646, 14: 1.828}
    elif n == 8:
        return {9: 1.0, 10: 1.414, 11: 1.732, 12: 1.236