def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count)


def some_func_with_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count, reverse=True)


def some_func_with_min(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lst.count, reverse=True)


def some_func_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum of the elements in the tuple.
    """
    return sum(lst, key=lst.count)


def some_func_with_count(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the tuple.
    """
    return len(lst)


def some_func_with_sum_and_count(lst):
    """
    Given a list of tuples, write a function that returns the sum and the number of elements in the tuple.
    """
    return sum(lst, key=lst.count, reverse=True) + sum(lst, key=lst.count, reverse=True)


def some_func_with_count_and_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum and the number of elements in the tuple.
    """
    return sum(lst, key=lst.count, reverse=True) + sum(lst, key=lst.count, reverse=True) + sum(lst, key=lst.count, reverse=True)


def some_func_with_sum_and_count_and_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum and the number of elements in the tuple.
    """
    return sum(lst, key=lst.count, reverse=True) + sum(lst, key=lst.count, reverse=True) + sum(lst, key=lst