def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[0]


def tuple_extract_with_last(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    return min(lst, key=lambda x: x[1])[0]


def tuple_extract_with_last_with_first(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_first_with_last(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    return min(lst, key=lambda x: x[1])[1]


def tuple_extract_with_last_with_first_with_last(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_first_with_last_with_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    return min(lst, key=lambda x: x[1])[1]


def tuple_extract_with_last_with_first_with_last(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[