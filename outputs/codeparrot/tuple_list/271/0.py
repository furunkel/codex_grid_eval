def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[0]


def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[1])[0]


def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[0]


def tuple_extract_with_avg(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the average eleventh value.
    """
    return sum(lst)/len(lst)


def tuple_extract_with_std(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the standard deviation.
    """
    return math.sqrt(sum(lst)/len(lst))


def tuple_extract_with_var(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the variable.
    """
    return math.sqrt(sum(lst)/len(lst))


def tuple_extract_with_median(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the median.
    """
    return math.median(lst)


def tuple_extract_with_minmax(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest and largest values.
    """
    return min(lst, key=lambda x: x[1])[0]


def tuple_extract_with_median_with_minmax(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the median and the min