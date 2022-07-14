def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lst.count)


def some_func_with_args(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lst.count, args=lst[1:])


def some_func_with_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lst.count, kwargs=lst[1:])


def some_func_with_args_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lst.count, args=lst[1:], kwargs=lst[1:])


def some_func_with_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lst.count, kwargs=lst[1:], kwargs_kwargs=lst[1:])


def some_func_with_args_kwargs_kwargs(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lst.count, kwargs_kwargs=lst[1:], kwargs_kwargs_kwargs=lst[1:])


def some_func_with_kwargs_args(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lst.count, args=lst[1:], kwargs_args=lst[1:])


def some_func_with_args_kwargs_args(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest eleventh value.
   