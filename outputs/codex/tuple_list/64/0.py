
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
    return min(lst, key=lambda x: x[1])[0]


def fibonacci_recursive(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
    if len(lst) == 1:
        return lst[0][0]
    else:
        return min(lst[0], fibonacci_recursive(lst[1:]), key=lambda x: x[1])[0]


def fibonacci_recursive_2(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
    if len(lst) == 1:
        return lst[0][0]
    else:
        return min(lst[0], fibonacci_recursive_2(lst[1:]), key=lambda x: x[1])[0]


def fibonacci_recursive_3(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
    if len(lst) == 1:
        return lst[0][0]
    else:
        return min(lst[0], fibonacci_recursive_3(lst[1:]), key=lambda x: x[1])[0]


def fibonacci_recursive_4(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
    if len(lst) == 1:
        return lst[0][0]
    else:
        return min(lst[0], fibonacci_recursive_4(lst[1:]), key=lambda x: x[1])[0]


def fibonacci_recursive_5(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
    if len(lst) == 1:
       