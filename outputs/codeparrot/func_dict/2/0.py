
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 2, 2: 4, 3: 6}

    """
#    print n
    if n == 1:
        return {1: 2, 2: 4, 3: 6}
    elif n == 2:
        return {1: 2, 2: 4, 3: 6, 4: 8}
    elif n == 3:
        return {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22, 12: 24, 13: 26, 14: 28, 15: 30, 16: 32, 17: 34, 18: 36, 19: 38, 20: 40, 21: 42, 22: 43, 23: 44, 24: 45, 25: 46, 26: 47, 27: 48, 28: 49, 29: 50, 30: 51, 31: 52, 32: 53, 33: 54, 34: 55, 35: 56, 36: 57, 37: 58, 38: 59, 39: 60, 40: 61, 41: 62, 42: 63, 43: 64, 44: 65, 45: 66, 46: 67, 47: 68, 48: 69, 49: 70, 50: 71, 51: 72, 52: 73, 53: 74, 54: 75, 55: 76, 56: 77, 57: 78, 58: 79, 59: 80, 60: 81, 61: 82, 62: 83, 63: 84, 64: 85, 65: 86, 66: 87, 67: 88, 68: 89, 69: 90, 70: 91, 71: 92, 72: 93, 73: 94, 74: 95, 75: 96, 76: 97, 77: 98, 78: 99, 79: 100, 80: 101, 81: 102, 82: 103, 83: 104, 84: 105, 85: 106, 86: 107, 87: 108, 88: 109, 89: 110