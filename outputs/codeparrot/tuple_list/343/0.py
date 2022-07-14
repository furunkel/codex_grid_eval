def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[0]


def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[1])[0]


def tuple_extract_with_average(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the average eleventh value.
    """
    return sum(lst)/len(lst)


def tuple_extract_with_variance(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the variance eleventh value.
    """
    return sum(lst)/len(lst)


def tuple_extract_with_variance_with_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[1])[1]


def tuple_extract_with_variance_with_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_variance_with_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[1])[1]


def tuple_extract_with_variance_with_max(lst):
    """
    Given a list of