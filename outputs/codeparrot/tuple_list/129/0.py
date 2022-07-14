def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count)


def some_func_with_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count, reverse=True)


def some_func_with_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lst.count, reverse=True)


def some_func_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
    return sum(lst, key=lst.count)


def some_func_with_count(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
    return sum(lst, key=lst.count)


def some_func_with_sum_and_count(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value and the count of the first value.
    """
    return sum(lst, key=lst.count, reverse=True, count=1)


def some_func_with_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest eleventh value and the count of the first value.
    """
    return min(lst, key=lst.count, reverse=True, count=1, reverse_min=True)


def some_func_with_max_and_count(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value and the count of the first value.
    """
    return max(lst, key=lst.count, reverse=True, count=1, reverse_max=True)

