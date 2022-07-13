
def quintuples_sum_to_hundred(l: list):
    """
    quintuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred([1, 2, -3, 7, 2, 7])
    False
    """
    quintuples_sum_to_hundred_count = 0
    quintuples_sum_to_hundred_list = []
    for x in l:
        if quintuples_sum_to_hundred_count < 5:
            if quintuples_sum_to_hundred_count == 0:
                quintuples_sum_to_hundred_list.append(x)
                quintuples_sum_to_hundred_count += 1
            else:
                if quintuples_sum_to_hundred_list[-1] + x == 100:
                    quintuples_sum_to_hundred_list.append(x)
                    quintuples_sum_to_hundred_count += 1
                else:
                    quintuples_sum_to_hundred_count = 0
                    quintuples_sum_to_hundred_list.append(x)
        else:
            return False
    if quintuples_sum_to_hundred_count == 5:
        return True
    else:
        return False


def quintuples_sum_to_hundred_list(l: list):
    """
    quintuples_sum_to_hundred_list takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred_list([1, 2, -3, 7, 2, 7])
    False
    """
    quintuples_sum_to_hundred_count = 0
    quintuples_sum_to_hundred_