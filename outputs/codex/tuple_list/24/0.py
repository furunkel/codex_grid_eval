
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value.
    """
    return min(lst, key=lambda x: x[2])[0]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest third values.
    """
    return [x[1] for x in lst if x[2] == min(lst, key=lambda x: x[2])[2]]


def count_unique(lst):
    """
    Given a list of strings, write a function that returns the number of unique strings in the list.
    """
    return len(set(lst))


def count_unique_case_insensitive(lst):
    """
    Given a list of strings, write a function that returns the number of unique strings in the list, ignoring case.
    """
    return len(set(x.lower() for x in lst))


def remove_duplicates(lst):
    """
    Given a list of strings, write a function that returns a list of the strings with duplicates removed.
    """
    return list(set(lst))


def remove_duplicates_case_insensitive(lst):
    """
    Given a list of strings, write a function that returns a list of the strings with duplicates removed, ignoring case.
    """
    return list(set(x.lower() for x in lst))


def remove_duplicates_keep_order(lst):
    """
    Given a list of strings, write a function that returns a list of the strings with duplicates removed, preserving the order of the remaining items.
    """
    return list(OrderedDict.fromkeys(lst))


def remove_duplicates_keep_order_case_insensitive(lst):
    """
    Given a list of strings, write a function that returns a list of the strings with duplicates removed, preserving the order of the remaining items, ignoring case.
    """
    return list(OrderedDict.fromkeys(x.lower() for x in lst))


def remove_duplicates_keep_order_case_insensitive_and_sort(lst):
    """
