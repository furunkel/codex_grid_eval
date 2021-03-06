def doubles_sum_to_one(l: list):
    """
    doubles_sum_to_one takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one([1, 2, -3, 7, 2, 7])
    False
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0])


def doubles_sum_to_two(l: list):
    """
    doubles_sum_to_two takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two([1, 2, -3, 7, 2, 7])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0]) and sum(l[1:]) == len(l[0])


def doubles_sum_to_three(l: list):
    """
    doubles_sum_to_three takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three([1, 2, -3, 7, 2, 7])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0]) and sum(l[1:]) == len(l[0])


def doubles_sum_to_four(l: list):
    """
    doubles_sum_to_four takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to four, and False otherwise.

    >>> doubles_sum_to_four([1, 2, -3, 7, 2, 7])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0]) and sum(l[1:]) == len(l[0])


def doubles_sum_to_five(l: list):
    """
    doubles_sum_