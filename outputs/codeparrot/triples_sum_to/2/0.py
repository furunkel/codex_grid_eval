def doubles_sum_to_zero(l: list):
    """
    doubles_sum_to_zero takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> doubles_sum_to_zero([1, 2, -3, 7, 2, 7])
    False
    """
    if len(l) == 0:
        return False
    return sum(l) == 0


def doubles_sum_to_one(l: list):
    """
    doubles_sum_to_one takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one([1, 2, -3, 7, 2, 7])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == 1


def doubles_sum_to_zero_by_one(l: list):
    """
    doubles_sum_to_zero_by_one takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> doubles_sum_to_zero_by_one([1, 2, -3, 7, 2, 7])
    False
    """
    if len(l) == 0:
        return False
    return sum(l) == 0 and len(l) == 1


def doubles_sum_to_one_by_zero(l: list):
    """
    doubles_sum_to_one_by_zero takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one_by_zero([1, 2, -3, 7, 2, 7])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == 1 and len(l) == 0


def doubles_sum_to_zero_by_one_by_zero(l: list):
    """
    doubles_sum_to_zero_by_one_by_zero takes a list of integers