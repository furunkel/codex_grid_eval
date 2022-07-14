def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[1]


def test_func():
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(some_func(lst) for lst in [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def test_func_with_args():
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(some_func(lst) for lst in [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def test_func_with_kwargs():
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(some_func(lst) for lst in [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def test_func_with_args_kwargs():
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(some_func(lst) for lst in [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def test_func_with_kwargs_kwargs():
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(some_func(lst) for lst in [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def test_func_with_args_kwargs_kwargs():
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(some_func(lst) for lst in [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def test_func_with_kwargs_args():
    """
    Given a list of tuples