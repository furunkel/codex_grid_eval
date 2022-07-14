def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[0]


def some_func_with_args(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1]


def some_func_with_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1][0]


def some_func_with_args_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1][1]


def some_func_with_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1][1][0]


def some_func_with_args_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1][1][1]


def some_func_with_kwargs_args_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1][1][1]


def some_func_with_args_kwargs_args_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1][1][1][0]


def some_func_with_kwargs_kwargs_args