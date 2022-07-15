
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    d = {}
    for i in range(1, n + 1):
        d[i] = i - i
    return d

print(generate_dict(10))

#%%

"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
which contains every number.
"""

def generate_list_tuple(n):
    """
    With a given sequence of comma-separated numbers, write a program to generate a list and a tuple which contains
    every number.
    
    """
    l = n.split(',')
    t = tuple(l)
    return l, t

print(generate_list_tuple('1,2,3,4,5,6,7,8,9,10'))

#%%

"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
"""

class String:
    """
    Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    
    """
    def __init__(self):
        self.s = ''
    
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = String()
strObj.getString()
strObj.printString()

#%%

"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
"""

import math

def calc_value(d):
    """
    With a given sequence of comma-separated numbers, write a program to calculate and print the value according to
    the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H