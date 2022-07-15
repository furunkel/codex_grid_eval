
def quintuples_sum_to_three(l: list):
    """
    quintuples_sum_to_three takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quintuples_sum_to_three([1, 3, 5, 0])
    False
    """
    quintuples = [x for x in l if sum(x) == 3]
    return len(quintuples) == 5


def quintuples_sum_to_four(l: list):
    """
    quintuples_sum_to_four takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to four, and False otherwise.

    >>> quintuples_sum_to_four([1, 3, 5, 0])
    True
    """
    quintuples = [x for x in l if sum(x) == 4]
    return len(quintuples) == 4


def quintuples_sum_to_five(l: list):
    """
    quintuples_sum_to_five takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quintuples_sum_to_five([1, 3, 5, 0])
    False
    """
    quintuples = [x for x in l if sum(x) == 5]
    return len(quintuples) == 5


def quintuples_sum_to_six(l: list):
    """
    quintuples_sum_to_six takes a list of integers as an input.
    it returns True if there are 6 distinct elements in the list that
    sum to six, and False otherwise.

    >>> quintuples_sum_to_