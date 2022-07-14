def doubles_sum_to_one(l: list):
    """
    doubles_sum_to_one takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 2 and l[0] == l[1]


def doubles_sum_to_two(l: list):
    """
    doubles_sum_to_two takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 2 and l[0] == l[1] and l[0] == l[2]


def doubles_sum_to_three(l: list):
    """
    doubles_sum_to_three takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 3 and l[0] == l[1] and l[0] == l[2]


def doubles_sum_to_four(l: list):
    """
    doubles_sum_to_four takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to four, and False otherwise.

    >>> doubles_sum_to_four([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 4 and l[0] == l[1] and l[0] == l[2]


def doubles_sum_to_five(l: list):
    """
    doubles_sum_to_five takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_