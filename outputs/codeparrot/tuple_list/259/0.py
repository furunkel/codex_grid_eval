def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[0]


def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]


def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[1])[0]


def tuple_extract_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    return sum(lst, key=lambda x: x[1])[0]


def tuple_extract_with_avg(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    return sum(lst, key=lambda x: x[1])[1] / len(lst)


def tuple_extract_with_std(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    return math.sqrt(sum(lst, key=lambda x: x[1]))


def tuple_extract_with_var(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    return math.sqrt(sum(lst, key=lambda x: x[1]))


def tuple_extract_with_std_with_var(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    return math.sqrt(sum(lst,