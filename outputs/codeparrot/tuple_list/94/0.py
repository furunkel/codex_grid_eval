def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)


def fibonacci_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[-1]


def fibonacci_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.count)[-1]


def fibonacci_with_sum_of_values(lst):
    """
    Given a list of tuples, write a function that returns the sum of the values of the tuple with the largest second value.
    """
    return sum(lst, key=lst.count)


def fibonacci_with_sum_of_values_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the sum of the values of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[-1]


def fibonacci_with_sum_of_values_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the sum of the values of the tuple with the smallest second value.
    """
    return min(lst, key=lst.count)[-1]


def fibonacci_with_sum_of_values_with_max_value_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the sum of the values of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[-1]


def fibonacci_with_sum_of_values_with_max_value_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the sum of the values of the tuple with the largest second value.
    """
    return max(lst, key=lst.