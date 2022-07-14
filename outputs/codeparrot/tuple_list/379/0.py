def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)


def tuple_concat(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return tuple(lst)


def tuple_slice(lst, start, stop):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return tuple(lst[start:stop])


def tuple_slice_list(lst, start, stop):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return tuple(lst[start:stop])


def tuple_slice_dict(lst, start, stop):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return dict(lst[start:stop])


def tuple_slice_array(lst, start, stop):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return tuple(lst[start:stop])


def tuple_slice_string(lst, start, stop):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return str(lst[start:stop])


def tuple_slice_number(lst, start, stop):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return int(lst[start:stop])


def tuple_slice_dict_list(lst, start, stop):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return [tuple(lst[start:stop])]


def tuple_slice_array_list(lst, start, stop):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return [tuple(