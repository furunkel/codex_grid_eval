def quadruples_sum_to_five(l: list):
    """
    quadruples_sum_to_five takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quadruples_sum_to_five([1, 3, -2, 1, 5, 8])
    True
    """
    return sum(l) % 2 == 0


def quadruples_sum_to_three(l: list):
    """
    quadruples_sum_to_three takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quadruples_sum_to_three([1, 3, -2, 1, 5, 8])
    True
    """
    return sum(l) % 3 == 0


def quadruples_sum_to_two(l: list):
    """
    quadruples_sum_to_two takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two([1, 3, -2, 1, 5, 8])
    True
    """
    return sum(l) % 2 == 0


def quadruples_sum_to_three_and_four(l: list):
    """
    quadruples_sum_to_three_and_four takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to three and four, and False otherwise.

    >>> quadruples_sum_to_three_and_four([1, 3, -2, 1, 5, 8])
    True
    """
    return sum(l) % 4 == 0 and sum(l) % 4 == 1


def quadruples_sum_to_two_and_three(l: list):
    """
    quadruples_sum_to_two_and_three takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two and three, and False otherwise.

    >>> quadruples