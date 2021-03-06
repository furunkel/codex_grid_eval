def quadruples_sum_to_five(l: list):
    """
    quadruples_sum_to_five takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quadruples_sum_to_five([1, 2, -3, 7, 2, 7])
    False
    """
    return sum(l) % 2 == 0


def quadruples_sum_to_three(l: list):
    """
    quadruples_sum_to_three takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quadruples_sum_to_three([1, 2, -3, 7, 2, 7])
    True
    """
    return sum(l) % 3 == 0


def quadruples_sum_to_two(l: list):
    """
    quadruples_sum_to_two takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two([1, 2, -3, 7, 2, 7])
    True
    """
    return sum(l) % 2 == 0


def quadruples_sum_to_three(l: list):
    """
    quadruples_sum_to_three takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quadruples_sum_to_three([1, 2, -3, 7, 2, 7])
    True
    """
    return sum(l) % 3 == 0


def quadruples_sum_to_two_with_one_element(l: list):
    """
    quadruples_sum_to_two_with_one_element takes a list of integers as
    an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two_with_one_element([1, 2, -3,