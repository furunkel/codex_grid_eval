def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return max(lst, key=lambda x: x[0])[0]


def tuple_extract_with_last(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(lst, key=lambda x: x[0])[0]


def tuple_extract_with_first(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[0]


def tuple_extract_with_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value and the smallest last value.
    """
    return max(lst, key=lambda x: x[0])[0], max(lst, key=lambda x: x[1])[0]


def tuple_extract_with_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first and the largest last value.
    """
    return min(lst, key=lambda x: x[0], key=lambda x: x[1])


def tuple_extract_with_last_and_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first and the largest last value and the smallest last value.
    """
    return min(lst, key=lambda x: x[0], key=lambda x: x[1], reverse=True)


def tuple_extract_with_first_and_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first and the largest last value and the smallest last value.
    """
    return min(lst, key=lambda x: x[0], key=lambda x: x[1],