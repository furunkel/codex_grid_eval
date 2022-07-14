def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)


def extract_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)[-1]


def extract_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)[-1]


def extract_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return min(lst, key=lst.count)[-1]


def extract_value_from_list_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return sum(lst)/len(lst)


def extract_value_from_list_with_variance(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return sum(lst)/len(lst)


def extract_value_from_list_with_std(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return math.sqrt(sum(lst)/len(lst))


def extract_value_from_list_with_median(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return math.median(lst)/len(lst)


def extract_value_from_list_with_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of