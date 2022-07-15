def quadruples_sum_to_one(l: list):
    """
    quadruples_sum_to_one takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to one, and False otherwise.

    >>> quadruples_sum_to_one([1])
    False
    """
    if len(l) == 0:
        return False
    return sum(l) == 1


def quadruples_sum_to_two(l: list):
    """
    quadruples_sum_to_two takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two([1, 2, 3])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == 2


def quadruples_sum_to_three(l: list):
    """
    quadruples_sum_to_three takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quadruples_sum_to_three([1, 2, 3])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == 3


def quadruples_sum_to_four(l: list):
    """
    quadruples_sum_to_four takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to four, and False otherwise.

    >>> quadruples_sum_to_four([1, 2, 3])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == 4


def quadruples_sum_to_five(l: list):
    """
    quadruples_sum_to_five takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quadruples_sum_to_five([1, 2, 3])
    True
    """
    if len(l) == 0