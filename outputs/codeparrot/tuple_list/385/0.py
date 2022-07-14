def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return tuple(lst[-1])


def tuple_extract_with_last(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return tuple(lst[-2])


def tuple_extract_with_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value.
    """
    return tuple(lst[0])


def tuple_extract_with_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value and the second value.
    """
    return tuple(lst[-2]) + tuple_extract_with_first(lst[-1])


def tuple_extract_with_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value and the second value.
    """
    return tuple(lst[0]) + tuple_extract_with_last(lst[-1]) + tuple_extract_with_first(lst[-2])


def tuple_extract_with_first_and_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value and the second value.
    """
    return tuple(lst[0]) + tuple_extract_with_first_and_last(lst[-1]) + tuple_extract_with_last_and_first(lst[-2])


def tuple_extract_with_first_and_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value and the second value.
    """
    return tuple(lst[0]) + tuple_extract_with_first_and_last(lst[-1]) + tuple_extract_with_last_and_first(lst[-2])


def tuple_extract_with_first_and_last_and_first(lst):
    """
    Given a list of