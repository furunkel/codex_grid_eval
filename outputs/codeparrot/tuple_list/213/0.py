def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lst[-1])[0]


def some_func_with_last_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest last value.
    """
    return max(lst, key=lst[-1])[1]


def some_func_with_first_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest first value.
    """
    return min(lst, key=lst[0])[0]


def some_func_with_last_value_and_first_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest last value and the first value.
    """
    return max(lst, key=lst[-1])[1]


def some_func_with_first_value_and_last_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest first value and the first value.
    """
    return min(lst, key=lst[0])[1]


def some_func_with_last_value_and_first_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest last value and the first value.
    """
    return max(lst, key=lst[-1])[1]


def some_func_with_first_value_and_last_value_and_first_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest first value and the first value.
    """
    return min(lst, key=lst[0])[1]


def some_func_with_last_value_and_first_value_and_last_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest last value and the first value.
    """
    return max(lst, key=lst[-1])[1]


