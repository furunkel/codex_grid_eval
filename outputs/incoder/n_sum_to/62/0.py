
def quintuples_sum_to_two(l: list):
    """
    quintuples_sum_to_two takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quintuples_sum_to_two([1, 2, -3, 7, 2, 7])
    False
    """
    quintuples = [(x, y) for x in l for y in l if x + y == 2]
    return len(quintuples) == 5


def quintuples_sum_to_three(l: list):
    """
    quintuples_sum_to_three takes a list of integers as an input.
    it returns True if there are 6 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quintuples_sum_to_three([1, 2, -3, 7, 2, 7])
    True
    """
    quintuples = [(x, y) for x in l for y in l if x + y == 3]
    return len(quintuples) == 6


def quintuples_sum_to_four(l: list):
    """
    quintuples_sum_to_four takes a list of integers as an input.
    it returns True if there are 7 distinct elements in the list that
    sum to four, and False otherwise.

    >>> quintuples_sum_to_four([1, 2, -3, 7, 2, 7])
    False
    """
    quintuples = [(x, y) for x in l for y in l if x + y == 4]
    return len(quintuples) == 7


def quintuples_sum_to_five(l: list):
    """
    quintuples_sum_to_five takes a list of integers as an input.
    it returns True if there are 8 distinct elements in the list that
    sum to 