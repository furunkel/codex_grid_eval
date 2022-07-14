def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[1])[1]


def tuple_extract_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the mean twelfth value.
    """
    return sum(lst)/len(lst)


def tuple_extract_with_median(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the median twelfth value.
    """
    return median(lst)/len(lst)


def tuple_extract_with_variance(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the variance twelfth value.
    """
    return variance(lst)/len(lst)


def tuple_extract_with_standard_deviation(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the standard deviation twelfth value.
    """
    return std(lst)/len(lst)


def tuple_extract_with_variance_deviation(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the variance twelfth value.
    """
    return variance(lst)/len(lst)


def tuple_extract_with_standard_deviation_deviation(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the standard deviation twelfth value.
    """
    return std(lst)/len