
def quintuples_sum_to_three(l: list):
    """
    quintuples_sum_to_three takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quintuples_sum_to_three([1, 2, -3, 7, 2, 7])
    False
    """
    quintuples = [x for x in l if x != -3]
    quintuples.sort()
    quintuples.reverse()
    quintuples_sum = 0
    for x in quintuples:
        quintuples_sum += x
        if quintuples_sum == 3:
            return True
    return False


def quintuples_sum_to_five(l: list):
    """
    quintuples_sum_to_five takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quintuples_sum_to_five([1, 2, -3, 7, 2, 7])
    True
    """
    quintuples = [x for x in l if x != -3]
    quintuples.sort()
    quintuples.reverse()
    quintuples_sum = 0
    for x in quintuples:
        quintuples_sum += x
        if quintuples_sum == 5:
            return True
    return False


def quintuples_sum_to_nine(l: list):
    """
    quintuples_sum_to_nine takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to nine, and False otherwise.

    >>> quintuples_sum_to_