def doubles_sum_to_three(l: list):
    """
    doubles_sum_to_three takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three([1, 2, -3, 7, 2, 7])
    True
    """
    return len(l) == 2 and sum(l) == 3


def doubles_sum_to_two(l: list):
    """
    doubles_sum_to_two takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two([1, 2, -3, 7, 2, 7])
    True
    """
    return len(l) == 2 and sum(l) == 2


def doubles_sum_to_three_with_one_element(l: list):
    """
    doubles_sum_to_three_with_one_element takes a list of integers as an
    input.
    it returns True if there are 2 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three_with_one_element([1, 2, -3, 7, 2, 7])
    True
    """
    return len(l) == 2 and sum(l) == 3 and sum(l) == 2


def doubles_sum_to_two_with_one_element(l: list):
    """
    doubles_sum_to_two_with_one_element takes a list of integers as an
    input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two_with_one_element([1, 2, -3, 7, 2, 7])
    True
    """
    return len(l) == 2 and sum(l) == 2 and sum(l) == 1


def doubles_sum_to_three_with_two_elements(l: list):
    """
    doubles_sum_to_three_with_two_elements takes a list of integers as an
    input.
    it returns True if