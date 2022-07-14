def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return max(lst, key=lst.count)[1]


def fibonacci_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[0]


def fibonacci_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return min(lst, key=lst.count)[0]


def fibonacci_with_sum_of_squares(lst):
    """
    Given a list of tuples, write a function that returns the sum of the squares of the given list.
    """
    return sum(lst)


def fibonacci_with_sum_of_squares_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the sum of the squares of the given list.
    """
    return max(lst, key=lst.count)[1]


def fibonacci_with_sum_of_squares_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the sum of the squares of the given list.
    """
    return min(lst, key=lst.count)[0]


def fibonacci_with_sum_of_squares_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the sum of the squares of the given list.
    """
    return max(lst, key=lst.count)[1]


def fibonacci_with_sum_of_squares_with_min_and_max_value(lst):
    """
    Given a list of tuples, write a function that returns the sum of the squares of the given list.
    """
    return min(lst, key=lst.count)[0], max(lst, key=lst.count)[1]


def fibonacci_with_sum_of_squares