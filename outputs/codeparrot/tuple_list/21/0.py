def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[0]


def test_func():
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return some_func(lst)


def test_func_with_args():
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return some_func(lst)


def test_func_with_kwargs():
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return some_func(lst, kwargs={'a': 1, 'b': 2})


def test_func_with_args_kwargs():
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return some_func(lst, kwargs={'a': 1, 'b': 2}, kwargs_a=1, kwargs_b=2)


def test_func_with_kwargs_kwargs():
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return some_func(lst, kwargs={'a': 1, 'b': 2}, kwargs_a=1, kwargs_b=2, kwargs_c=3)


def test_func_with_kwargs_kwargs():
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return some_func(lst, kwargs={'a': 1, 'b': 2}, kwargs_a=1, kwargs_b=2, kwargs_c=3, kwargs_d=4)


def test_func_with_kwargs_kwargs_kwargs():
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return some_func(lst, kwargs={'a': 1, 'b': 2}, kwargs_a=1, kwargs_b=2, kwargs_c=3, kwargs