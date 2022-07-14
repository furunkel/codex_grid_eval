def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count)


def some_func_with_max_twelfth(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count, reverse=True)


def some_func_with_max_twelfth_and_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value and the minimum value.
    """
    return max(lst, key=lst.count, reverse=True, key_func=lambda x: x[1])


def some_func_with_max_twelfth_and_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value and the maximum value.
    """
    return max(lst, key=lst.count, reverse=True, key_func=lambda x: x[1], reverse_func=lambda x: x[1])


def some_func_with_max_twelfth_and_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value and the minimum value.
    """
    return max(lst, key=lst.count, reverse=True, key_func=lambda x: x[1], reverse_func=lambda x: x[1], reverse_func=lambda x: x[1])


def some_func_with_max_twelfth_and_min_and_max_and_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value and the minimum value.
    """
    return max(lst, key=lst.count, reverse=True, key_func=lambda x: x[1], reverse_func=lambda x: x[1], reverse_func=lambda