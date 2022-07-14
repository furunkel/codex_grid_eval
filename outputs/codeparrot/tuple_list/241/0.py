def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest third value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest third value.
    """
    return min(lst, key=lambda x: x[1])[1]


def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_avg(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the average third value.
    """
    return sum(lst)/len(lst)


def tuple_extract_with_std(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the standard third value.
    """
    return math.sqrt(sum(lst)/len(lst))


def tuple_extract_with_var(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the variance third value.
    """
    return math.sqrt(sum(lst)/len(lst))


def tuple_extract_with_median(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the median third value.
    """
    return math.median(lst)/len(lst)


def tuple_extract_with_minmax(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest third value.
    """
    return min(lst, key=lambda x: x[1])[1]


def tuple_extract_with_maxmin(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return