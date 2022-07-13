
def quintuples_sum_to_two(l: list):
    """
    quintuples_sum_to_two takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quintuples_sum_to_two([1, 3, 5, 0])
    False
    """
    quintuples = []
    for x in l:
        if x not in quintuples:
            quintuples.append(x)
        else:
            return False
    return True


def quintuples_sum_to_three(l: list):
    """
    quintuples_sum_to_three takes a list of integers as an input.
    it returns True if there are 6 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quintuples_sum_to_three([1, 3, 5, 0])
    True
    """
    quintuples = []
    for x in l:
        if x not in quintuples:
            quintuples.append(x)
        else:
            return False
    return True


def quintuples_sum_to_four(l: list):
    """
    quintuples_sum_to_four takes a list of integers as an input.
    it returns True if there are 7 distinct elements in the list that
    sum to four, and False otherwise.

    >>> quintuples_sum_to_four([1, 3, 5, 0])
    True
    """
    quintuples = []
    for x in l:
        if x not in quintuples:
            quintuples.append(x)
        else:
            return False
    return True


def quintuples_sum_to_five(l: list):
    """
    quintuples_sum_to_five takes a list of integers as an input.
    it 