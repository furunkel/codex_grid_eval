def doubles_sum_to_hundred(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred([1])
    False
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0])


def doubles_sum_to_hundred_with_sum(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_with_sum([1, 2, 3])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0]) and sum(l) == len(l[1])


def doubles_sum_to_hundred_with_sum_with_sum(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_with_sum_with_sum([1, 2, 3])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0]) and sum(l) == len(l[1]) and sum(l) == len(l[2])


def doubles_sum_to_hundred_with_sum_with_sum_with_sum(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_with_sum_with_sum([1, 2, 3])
    True
    """
    if len(l) == 0:
        return