def quadruples_sum_to_hundred(l: list):
    """
    quadruples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred([1, 2, -3, 7, 2, 7])
    False
    """
    if len(l) == 0:
        return False
    if len(l) == 1:
        return True
    if len(l) == 2:
        return True
    if len(l) == 3:
        return True
    if len(l) == 4:
        return True
    return False


def quadruples_sum_to_hundred_with_sum(l: list):
    """
    quadruples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred_with_sum([1, 2, -3, 7, 2, 7])
    True
    """
    if len(l) == 0:
        return False
    if len(l) == 1:
        return True
    if len(l) == 2:
        return True
    if len(l) == 3:
        return True
    if len(l) == 4:
        return True
    return False


def quadruples_sum_to_hundred_with_sum_with_sum(l: list):
    """
    quadruples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred_with_sum_with_sum([1, 2, -3, 7, 2, 7])
    True
    """
    if len(l) == 0:
        return False
    if len(l) == 1:
        return True
    if len(l) == 2:
        return True
    if len(l) == 3:
        return True
    if len(l) == 4:
        return True
   