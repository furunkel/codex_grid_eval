def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count)


def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count)[-1]


def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    return min(lst, key=lst.count)[0]


def tuple_extract_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return sum(lst, key=lst.count)


def tuple_extract_with_avg(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the average first value.
    """
    return sum(lst, key=lst.count) / len(lst)


def tuple_extract_with_std(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return math.sqrt(sum(lst, key=lst.count)) / len(lst)


def tuple_extract_with_var(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return math.sqrt(sum(lst, key=lst.count)) / len(lst)


def tuple_extract_with_std_var(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return math.sqrt(sum(lst, key=lst.count)) / len(lst)


def tuple_extract_with_var_std(lst):
    """
    Given a list of tuples, write a function that returns the twe