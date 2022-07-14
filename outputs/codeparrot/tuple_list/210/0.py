def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)[0]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)[-1]


def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)[-2]


def get_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)[-1]


def get_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return min(lst, key=lst.count)[-1]


def get_value_from_list_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return sum(lst)/len(lst)


def get_value_from_list_with_std(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return math.sqrt(sum(lst)/len(lst))


def get_value_from_list_with_median(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return math.median(lst)/len(lst)


def get_value_from_list_with_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return min(lst), max(lst)


def get_value_from_