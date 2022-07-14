def some_func(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)[0]


def some_func_with_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)[-1]


def some_func_with_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
    return min(lst, key=lst.count)[0]


def some_func_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest sum.
    """
    return sum(lst, key=lst.count)[-1]


def some_func_with_count(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest count.
    """
    return sum(lst, key=lst.count)[-1]


def some_func_with_sum_and_count(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest sum and count.
    """
    return sum(lst, key=lst.count)[-1], sum(lst, key=lst.count)[-1]


def some_func_with_count_and_sum(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest count and count.
    """
    return sum(lst, key=lst.count)[-1], sum(lst, key=lst.count)[-1]


def some_func_with_sum_and_count_and_sum(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest sum and count and count.
    """
    return sum(lst, key=lst.count)[-1], sum(lst, key=lst.count)[-1], sum(lst, key=lst