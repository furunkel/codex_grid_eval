def f(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[0]


def f_with_args(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[1]


def f_with_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[1][0]


def f_with_args_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[1][1]


def f_with_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[1][1][1]


def f_with_args_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[1][1][1]


def f_with_kwargs_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[1][1][1][1]


def f_with_args_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[1][1][1][1]


def f_with_kwargs_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the