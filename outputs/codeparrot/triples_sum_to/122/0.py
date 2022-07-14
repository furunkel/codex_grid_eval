def doubles_sum_to_hundred(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred([1, 2, -3, 7, 2, 7])
    False
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0])


def doubles_sum_to_hundred_sorted(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_sorted([1, 2, -3, 7, 2, 7])
    False
    """
    if len(l) == 0:
        return False
    return sorted(l, key=doubles_sum_to_hundred_key)


def doubles_sum_to_hundred_sorted_sorted(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_sorted_sorted([1, 2, -3, 7, 2, 7])
    False
    """
    if len(l) == 0:
        return False
    return sorted(l, key=doubles_sum_to_hundred_key_sorted)


def doubles_sum_to_hundred_sorted_sorted_sorted(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_sorted_sorted_sorted([1, 2, -3, 7, 2, 7])
    False
    """
    if len(l) == 0:
        return False
    return sorted(l