def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_last(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[0]


def tuple_extract_with_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[0])[0]


def tuple_extract_with_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value and the first value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1], key=lambda x: x[0])


def tuple_extract_with_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value and the first value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[1], reverse=True)[0], key=lambda x: x[0])


def tuple_extract_with_first_and_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value and the first value of the tuple with the smallest twelfth value and the first value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[1], reverse=True)[0], key=lambda x: x[0])


def tuple_extract_with_last_and_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple