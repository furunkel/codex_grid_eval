
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return min(lst, key=lambda x: x[2])[-1]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return [x[1] for x in lst]


def remove_duplicates(lst):
    """
    Given a list of tuples, write a function that returns a list of tuples with the duplicates removed.
    """
    return list(set(lst))


def swap_first_last(lst):
    """
    Given a list of tuples, write a function that swaps the first and last elements of each tuple.
    """
    return [(x[-1], x[1], x[2], x[3], x[0]) for x in lst]


def sort_by_third_element(lst):
    """
    Given a list of tuples, write a function that sorts the list by the third element in each tuple.
    """
    return sorted(lst, key=lambda x: x[2])


def sort_by_last_element(lst):
    """
    Given a list of tuples, write a function that sorts the list by the last element in each tuple.
    """
    return sorted(lst, key=lambda x: x[-1])


def sort_by_first_element(lst):
    """
    Given a list of tuples, write a function that sorts the list by the first element in each tuple.
    """
    return sorted(lst, key=lambda x: x[0])


def sort_by_second_element(lst):
    """
    Given a list of tuples, write a function that sorts the list by the second element in each tuple.
    """
    return sorted(lst, key=lambda x: x[1])


def sort_by_fourth_element(lst):
    """
    Given a list of tuples, write a function that sorts the list by the fourth element in each tuple.
    """
    return sorted(lst, key=lambda x: x[3])


def sort_by