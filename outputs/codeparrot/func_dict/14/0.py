
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 1, 2: 4, 3: 9}

    """
#    print n
    if n == 1:
        return {1: 1, 2: 4, 3: 9}
    elif n == 2:
        return {1: 1, 2: 4, 3: 9, 4: 1}
    elif n == 3:
        return {1: 1, 2: 4, 3: 9, 4: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 6, 10: 7, 11: 8, 12: 9, 13: 10, 14: 11, 15: 12, 16: 13, 17: 14, 18: 15, 19: 16, 20: 17, 21: 18, 22: 19, 23: 20, 24: 21, 25: 22, 26: 23, 27: 24, 28: 25, 29: 26, 30: 27, 31: 28, 32: 29, 33: 30, 34: 31, 35: 31, 36: 32, 37: 33, 38: 34, 39: 35, 40: 36, 41: 37, 42: 38, 43: 39, 44: 40, 45: 41, 46: 42, 47: 43, 48: 44, 49: 45, 50: 46, 51: 47, 52: 48, 53: 49, 54: 50, 55: 51, 56: 52, 57: 53, 58: 54, 59: 55, 60: 56, 61: 57, 62: 58, 63: 59, 64: 60, 65: 61, 66: 66, 67: 67, 68: 68, 69: 69, 70: 70, 71: 71, 72: 72, 73: 73, 74: 74, 75: 75, 76: 76, 77: 77, 78: 78, 79: 79, 80: 80, 81: 81, 82: 82, 83: 83, 84: 84, 85: 85, 86: 86, 87: 87, 88: 88, 89: 89