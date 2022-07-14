def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[1]


def get_twelfth_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[-1]


def get_twelfth_value_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[-1]


def get_twelfth_value_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.count)[-1]


def get_twelfth_value_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
    return mean(lst, key=lst.count)[-1]


def get_twelfth_value_with_median(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
    return median(lst, key=lst.count)[-1]


def get_twelfth_value_with_variance(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
    return variance(lst, key=lst.count)[-1]


def get_twelfth_value_with_standard_deviation(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
    return standard_deviation(lst, key=lst.count)[-1]


def get_twelfth_value_with_variance_de