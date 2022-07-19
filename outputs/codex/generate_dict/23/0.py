
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    100
    Then, the output should be:
    {1: 1.0, 2: 1.414, 3: 1.732, 4: 2.0, 5: 2.236, 6: 2.449, 7: 2.646, 8: 2.828, 9: 3.0, 10: 3.162, 11: 3.317, 12: 3.464, 13: 3.606, 14: 3.742, 15: 3.873, 16: 4.0, 17: 4.123, 18: 4.243, 19: 4.359, 20: 4.472, 21: 4.583, 22: 4.69, 23: 4.796, 24: 4.899, 25: 5.0, 26: 5.099, 27: 5.196, 28: 5.292, 29: 5.385, 30: 5.477, 31: 5.568, 32: 5.657, 33: 5.745, 34: 5.831, 35: 5.916, 36: 6.0, 37: 6.083, 38: 6.164, 39: 6.245, 40: 6.325, 41: 6.403, 42: 6.481, 43: 6.557, 44: 6.633, 45: 6.708, 46: 6.782, 47: 6.856, 48: 6.928, 49: 7.0, 50: 7.071, 51: 7.141, 52: 7.211, 53: 7.28, 54: 7.348, 55: 7.416, 56: 7.483, 57: 7.55, 58: 7.616, 59: 7.681, 60: 7.746, 61: 7.81, 62: 7.874, 63: 7.937, 64: 8.0, 65: 8.062, 66: 8.124, 67: 8.185, 68: 8.246, 69: 8.307, 70: 8.367, 71: 8.426, 72: 8.485, 73: 8.544, 74: 8.602, 75: 8.66, 76: 8.718, 77: 8.775, 78: 8.832, 79: 8.888, 80: 8.944, 81: 9.0, 82: 9.055, 83: 9.11, 84: 9.165, 85: 9.22, 86: 9.274, 87: 9.327, 88: 9.381, 89: 9.434, 90: 9.487, 91: 9.539, 92: 9.592, 93: 9.644, 94: 9.695, 95: 9.747, 96: 9.798, 97: 9.849, 98: 9.899, 99: 9.95, 100: 10.0}

    """
    return {i: sqrt(i) for i in range(1, n+1)}


def generate_dict_2(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    """
    return {i: i*i for i in range(1, n+1)}


def generate_dict_3(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i*i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    8
    Then, the output should be:
    {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}
    """
    return {i: i*i*i for i in range(1, n+1)}


def generate_dict_4(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i*i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    8
    Then, the output should be:
    {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}
    """
    return {i: i*i*i for i in range(1, n+1)}


def generate_dict_5(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i,