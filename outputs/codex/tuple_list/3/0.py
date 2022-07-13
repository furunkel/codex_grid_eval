
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[0]

# print(some_func([(1,2), (3,4), (5,6)]))

def some_func2(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[0]

# print(some_func2([(1,2), (3,4), (5,6)]))

def some_func3(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]

# print(some_func3([(1,2), (3,4), (5,6)]))

def some_func4(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1]

# print(some_func4([(1,2), (3,4), (5,6)]))

def some_func5(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest first value.
    """
    return max(lst, key=lambda x: x[0])[0]

# print(some_func5([(1,2), (3,4), (5,6)]))

def some_func6(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return max(lst, key=lambda x: x[1])[0]

# print(some_func6([(1,2), (3,4), (5,6)]))

def some_func7(lst):
    """
    Given a list of tuples