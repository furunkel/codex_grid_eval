
def quintuples_sum_to_one(l: list):
    """
    quintuples_sum_to_one takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to one, and False otherwise.

    >>> quintuples_sum_to_one([1, 3, -2, 1, 5, 8])
    False
    """
    quintuples_sum_to_one_helper(l, 5, 0)
    return True


def quintuples_sum_to_one_helper(l: list, sum: int, count: int):
    """
    quintuples_sum_to_one_helper takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to one, and False otherwise.

    >>> quintuples_sum_to_one_helper([1, 3, -2, 1, 5, 8], 5, 0)
    True
    """
    if count == 5:
        return True
    if sum == 0:
        return False
    if sum < 0:
        return False
    if l[count] == 0:
        return False
    if l[count] == 1:
        return True
    if l[count] == 2:
        return quintuples_sum_to_one_helper(l, sum - 1, count + 1)
    if l[count] == 3:
        return quintuples_sum_to_one_helper(l, sum - 2, count + 1)
    if l[count] == 4:
        return quintuples_sum_to_one_helper(l, sum - 3, count + 1)
    if l[count] == 5:
        return quintuples_sum_to_one_helper(l, sum - 4, count + 1)
    if l[count] == 6:
        return quintuples_sum_to_one_helper(l, sum - 5, count + 1)


def quintuples_sum