
def quintuples_sum_to_hundred(l: list):
    """
    quintuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred([1, 3, -2, 1, 5, 8])
    False
    """
    quintuples_sum_to_hundred_helper(l, 0, 0, 0)
    return True


def quintuples_sum_to_hundred_helper(l: list, sum: list, count: int, max_count: int):
    """
    quintuples_sum_to_hundred_helper takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred_helper([1, 3, -2, 1, 5, 8], [], 0, 0)
    False
    >>> quintuples_sum_to_hundred_helper([1, 3, -2, 1, 5, 8], [], 1, 0)
    True
    >>> quintuples_sum_to_hundred_helper([1, 3, -2, 1, 5, 8], [], 2, 0)
    True
    >>> quintuples_sum_to_hundred_helper([1, 3, -2, 1, 5, 8], [], 3, 0)
    True
    >>> quintuples_sum_to_hundred_helper([1, 3, -2, 1, 5, 8], [], 4, 0)
    True
    >>> quintuples_sum_to_hundred_helper([1, 3, -2, 1, 5, 8], [], 5, 0)
    True
    >>> quintuples_sum_to_hundred_helper([1, 3, -2, 1, 5, 8], [], 6, 0)
    True
    >>> quintuples_sum_to_hundred_helper([1, 3, -2, 1, 5, 8