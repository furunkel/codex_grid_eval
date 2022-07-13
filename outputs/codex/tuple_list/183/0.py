
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[11])[2]

# print(some_func(lst))

# ----------------------------------------------------------------------------------------------------------------------

# Write a function that takes a list of tuples and returns a list of tuples with the first value of each tuple multiplied by 2.

lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

def some_func(lst):
    """
    Given a list of tuples, write a function that returns a list of tuples with the first value of each tuple multiplied by 2.
    """
    return [(x[0] * 2, x[1], x[2]) for x in lst]

# print(some_func(lst))

# ----------------------------------------------------------------------------------------------------------------------

# Write a function that takes a list of tuples and returns a list of tuples with the first value of each tuple multiplied by 2 and the second value of each tuple multiplied by 3.

lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

def some_func(lst):
    """
    Given a list of tuples, write a function that returns a list of tuples with the first value of each tuple multiplied by 2 and the second value of each tuple multiplied by 3.
    """
    return [(x[0] * 2, x[1] * 3, x[2]) for x in lst]

# print(some_func(lst))

# ----------------------------------------------------------------------------------------------------------------------

# Write a function that takes a list of tuples and returns a list of tuples with the first value of each tuple multiplied by 2, the second value of each tuple multiplied by 3, and the third value of each tuple multiplied by 4.

lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

def some_func(lst):
    """
    Given a list of tuples, write a function that returns a list of tuples with the first value of each tuple multiplied by 2, the second value of each tuple multiplied by 3, and the third value of each tuple multiplied by 4.
    """
    return [(x[0] * 2,