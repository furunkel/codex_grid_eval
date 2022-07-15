def quintuples_sum_to_hundred(l: list):
    """
    quintuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred([1, 3, -2, 1, 5, 8])
    False
    """
    return sum(l) % 2 == 0


def quintuples_sum_to_hundred_with_one_element(l: list):
    """
    quintuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred_with_one_element([1, 3, -2, 1, 5, 8])
    True
    """
    return sum(l) % 2 == 1


def quintuples_sum_to_hundred_with_two_elements(l: list):
    """
    quintuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred_with_two_elements([1, 3, -2, 1, 5, 8])
    True
    """
    return sum(l) % 2 == 2


def quintuples_sum_to_hundred_with_three_elements(l: list):
    """
    quintuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred_with_three_elements([1, 3, -2, 1, 5, 8])
    True
    """
    return sum(l) % 3 == 3


def quintuples_sum_to_hundred_with_four_elements(l: list):
    """
    quintuples_