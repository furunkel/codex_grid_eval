def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[0]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[1]


def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[0]


def get_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[1]


def get_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[1])[1]


def get_value_from_list_with_average(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return sum(lst)/len(lst)


def get_value_from_list_with_median(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst)/len(lst)


def get_value_from_list_with_variance(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return variance(lst)/len(lst)


def get_value_from_list_with_variance_with_min(lst):
    """
    Given a list