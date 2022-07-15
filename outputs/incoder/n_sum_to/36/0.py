
def quintuples_sum_to_one(l: list):
    """
    quintuples_sum_to_one takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to one, and False otherwise.

    >>> quintuples_sum_to_one([1, 3, 5, 0])
    False
    """
    quintuples = list(zip(l, l, l, l, l))
    quintuples.sort()
    quintuples.reverse()
    quintuples_sum = 0
    quintuples_sum_one = False
    for quintuple in quintuples:
        quintuples_sum += quintuple[0]
        if quintuples_sum == 1:
            quintuples_sum_one = True
            break
    return quintuples_sum_one


def quintuples_sum_to_one_2(l: list):
    """
    quintuples_sum_to_one_2 takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to one, and False otherwise.

    >>> quintuples_sum_to_one_2([1, 3, 5, 0])
    True
    """
    quintuples = list(zip(l, l, l, l, l))
    quintuples.sort()
    quintuples.reverse()
    quintuples_sum = 0
    quintuples_sum_one = False
    for quintuple in quintuples:
        quintuples_sum += quintuple[0]
        if quintuples_sum == 1:
            quintuples_sum_one = True
            break
    return quintuples_sum_one


def quintuple