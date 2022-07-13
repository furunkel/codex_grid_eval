
def quintuples_sum_to_five(l: list):
    """
    quintuples_sum_to_five takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quintuples_sum_to_five([1, 2, -3, 7, 2, 7])
    False
    """
    quintuples_sum_to_five = 0
    for i in l:
        quintuples_sum_to_five = quintuples_sum_to_five + i
        if quintuples_sum_to_five == 5:
            return True
    return False


def quintuples_sum_to_five_2(l: list):
    """
    quintuples_sum_to_five_2 takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quintuples_sum_to_five_2([1, 2, -3, 7, 2, 7])
    True
    """
    quintuples_sum_to_five_2 = 0
    for i in l:
        quintuples_sum_to_five_2 = quintuples_sum_to_five_2 + i
        if quintuples_sum_to_five_2 == 5:
            return True
    return False


def quintuples_sum_to_five_3(l: list):
    """
    quintuples_sum_to_five_3 takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quintuples_sum_to_five_3([1, 2, -3, 7, 2, 7])
    True
    """
    quintuples_