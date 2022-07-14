def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.count)


def some_func_with_args(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.count, args=lst[0])


def some_func_with_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.count, kwargs=lst[0])


def some_func_with_args_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.count, args=lst[0], kwargs=lst[1])


def some_func_with_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.count, kwargs=lst[0], kwargs=lst[1], kwargs_kwargs=lst[2])


def some_func_with_args_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.count, kwargs=lst[0], kwargs_kwargs=lst[1], kwargs_kwargs_kwargs=lst[2], kwargs_args=lst[3])


def some_func_with_kwargs_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.count, kwargs=lst[0], kwargs_kwargs=lst[1], kwargs_kwargs_kwargs=lst[2], kwargs_args=lst[3], kwargs_kwargs_args=