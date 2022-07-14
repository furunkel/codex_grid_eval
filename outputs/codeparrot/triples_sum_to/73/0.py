def doubles_sum_to_three(l: list):
    """
    doubles_sum_to_three takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 2 and sum(l) == 3


def doubles_sum_to_two(l: list):
    """
    doubles_sum_to_two takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 2 and sum(l) == 2


def doubles_sum_to_three_and_four(l: list):
    """
    doubles_sum_to_three_and_four takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to three and four, and False otherwise.

    >>> doubles_sum_to_three_and_four([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 3 and sum(l) == 3 and sum(l) == 4


def doubles_sum_to_two_and_three(l: list):
    """
    doubles_sum_to_two_and_three takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two and three, and False otherwise.

    >>> doubles_sum_to_two_and_three([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 2 and sum(l) == 2 and sum(l) == 3 and sum(l) == 4


def doubles_sum_to_two_and_four_and_five(l: list):
    """
    doubles_sum_to_two_and_four_and_five takes a list of integers as an input.
    it returns True if