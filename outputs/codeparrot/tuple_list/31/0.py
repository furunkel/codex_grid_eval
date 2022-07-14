def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[0]


def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[0]


def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value.
    """
    return min(lst, key=lst.count)[0]


def tuple_extract_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the sum of the values.
    """
    return sum(lst, key=lst.count)[0]


def tuple_extract_with_count(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the count of the values.
    """
    return sum(lst, key=lst.count)[0]


def tuple_extract_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the mean of the values.
    """
    return sum(lst, key=lst.count)[0]


def tuple_extract_with_std(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the standard deviation of the values.
    """
    return math.sqrt(sum(lst, key=lst.count)[0] / len(lst))


def tuple_extract_with_median(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the median of the values.
    """
    return math.median(lst, key=lst.count)[0]


def tuple_extract_with_min_max(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the minimum and maximum values.
    """
    return min(lst, key=lst.count)[0], max(lst