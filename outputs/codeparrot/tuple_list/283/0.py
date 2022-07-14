def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)


def tuple_extract_with_last(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)[-1]


def tuple_extract_with_first(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    return min(lst, key=lst.count)[0]


def tuple_extract_with_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first and the largest last value.
    """
    return max(lst, key=lst.count)[-1], lst[0]


def tuple_extract_with_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first and the largest last value.
    """
    return min(lst, key=lst.count)[0], lst[-1]


def tuple_extract_with_last_and_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first and the largest last value.
    """
    return min(lst, key=lst.count)[-1], lst[0]


def tuple_extract_with_first_and_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first and the largest last value.
    """
    return min(lst, key=lst.count)[-1], lst[0]


def tuple_extract_with_last_and_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first and the largest last value.
    """
    return