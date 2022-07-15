
def quintuples_sum_to_hundred(l: list):
    """
    quintuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred([1])
    False
    """
    quintuples_sum_to_hundred_count = 0
    for num in l:
        quintuples_sum_to_hundred_count += num
        if quintuples_sum_to_hundred_count > 100:
            return True
    return False


def quintuples_sum_to_hundred_count(l: list):
    """
    quintuples_sum_to_hundred_count takes a list of integers as an input.
    it returns the number of elements in the list that sum to hundred.

    >>> quintuples_sum_to_hundred_count([1])
    1
    """
    quintuples_sum_to_hundred_count = 0
    for num in l:
        quintuples_sum_to_hundred_count += num
    return quintuples_sum_to_hundred_count


def quintuples_sum_to_hundred_count_2(l: list):
    """
    quintuples_sum_to_hundred_count_2 takes a list of integers as an input.
    it returns the number of elements in the list that sum to hundred.
    it returns False if there are less than 5 elements in the list that sum to hundred.

    >>> quintuples_sum_to_hundred_count_2([1,2,3])
    1
    >>> quintuples_sum_to_hundred_count_2([1,2,4])
    0
    """
    quintuples_sum_to_