
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i**2) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

    """
#    n = int(n)
    if n < 1:
        return {}
    if n == 1:
        return {1: 1}
    if n == 2:
        return {2: 1, 3: 4, 4: 9, 5: 16, 6: 25, 7: 36, 8: 49, 9: 64}
    if n == 3:
        return {4: 1, 5: 9, 6: 16, 7: 25, 8: 36, 9: 49, 10: 64}
    if n == 4:
        return {5: 1, 6: 9, 7: 16, 8: 25, 9: 36, 10: 49, 11: 64}
    if n == 5:
        return {6: 1, 7: 9, 8: 16, 9: 25, 10: 36, 11: 49, 12: 64}
    if n == 6:
        return {7: 1, 8: 9, 9: 16, 10: 25, 11: 36, 12: 49, 13: 64}
    if n == 7:
        return {8: 1, 9: 9, 10: 16, 11: 25, 12: 36, 13: 49, 14: 64}
    if n == 8:
        return {9: 1, 10: 9, 11: 16, 12: 25, 13: 36, 14: 49, 15: 64}
    if n == 9:
        return {10: 1, 11: 9, 12: 16, 13: 25, 14: 36, 15: 49, 16: 64}
    if n == 10:
        return {11: 1, 12: 9, 13: 16, 14: 25, 15: 36, 16: 49, 17: 64}
    if n == 11:
        return {12: 1, 14: 9, 15: 16, 16: 25, 17: