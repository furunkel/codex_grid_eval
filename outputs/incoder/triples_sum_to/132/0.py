
def quintuples_sum_to_hundred(l: list):
    """
    quintuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred([1, 3, 5, 0])
    False
    """
    quintuples = []
    quintuples_sum = 0
    for x in l:
        if quintuples_sum + x not in quintuples:
            quintuples.append(quintuples_sum + x)
            quintuples_sum += x
        else:
            return False
    return True


def quintuples_sum_to_hundred_2(l: list):
    """
    quintuples_sum_to_hundred_2 takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred_2([1, 3, 5, 0])
    True
    """
    quintuples = []
    quintuples_sum = 0
    for x in l:
        if quintuples_sum + x not in quintuples:
            quintuples.append(quintuples_sum + x)
            quintuples_sum += x
        else:
            return True
    return False


def quintuples_sum_to_hundred_3(l: list):
    """
    quintuples_sum_to_hundred_3 takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred_3([1, 3, 5, 