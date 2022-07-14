def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[0]


def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[1])[0]


def tuple_extract_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the sum of the values.
    """
    return sum(lst, key=lambda x: x[1])


def tuple_extract_with_avg(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the average of the values.
    """
    return sum(lst, key=lambda x: x[1]) / len(lst)


def tuple_extract_with_std(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the standard deviation of the values.
    """
    return math.sqrt(sum(lst))


def tuple_extract_with_var(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the variance of the values.
    """
    return math.sqrt(sum(lst))


def tuple_extract_with_median(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the median of the values.
    """
    return math.median(lst)


def tuple_extract_with_min_max(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the minimum and maximum values.
    """
    return min(lst, key=lambda x: x[1]) if len(lst)