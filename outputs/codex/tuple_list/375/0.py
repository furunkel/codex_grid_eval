
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[0]

print(some_func([(1,2), (4,1), (9,10), (13,-3)]))

# Output: 4

# ----------------------------------------------------------------------------------------------------------------------

# Problem:
# Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]

print(some_func([(1,2), (4,1), (9,10), (13,-3)]))

# Output: 1

# ----------------------------------------------------------------------------------------------------------------------

# Problem:
# Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
    return max(lst, key=lambda x: x[0])[1]

print(some_func([(1,2), (4,1), (9,10), (13,-3)]))

# Output: -3

# ----------------------------------------------------------------------------------------------------------------------

# Problem:
# Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(lst, key=lambda x: x[1])[1]

print(some_func([(1,2), (4,1), (9,10), (13,-3)]))

# Output: 10

# ----------------------------------------------------------------------------------------------------------------------

# Problem:
# Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.

def some_func(lst):
    """