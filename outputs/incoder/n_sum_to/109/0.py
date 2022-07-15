
def quintuples_sum_to_five(l: list):
    """
    quintuples_sum_to_five takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quintuples_sum_to_five([1, 3, -2, 1, 5, 8])
    False
    """
    quintuples = []
    quintuples_sum = 0
    for x in l:
        quintuples_sum += x
        quintuples.append(quintuples_sum)
    quintuples.sort()
    quintuples_sum_to_five = False
    for x in quintuples:
        if quintuples_sum == x:
            quintuples_sum_to_five = True
    return quintuples_sum_to_five


def quintuples_sum_to_five_iterative(l: list):
    """
    quintuples_sum_to_five_iterative takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quintuples_sum_to_five_iterative([1, 3, -2, 1, 5, 8])
    False
    """
    quintuples = []
    quintuples_sum = 0
    for x in l:
        quintuples_sum += x
        quintuples.append(quintuples_sum)
    quintuples.sort()
    quintuples_sum_to_five = False
    for x in quintuples:
        if quintuples_sum == x:
            quintuples_sum_to_five = True
    return qu