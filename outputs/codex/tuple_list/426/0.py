
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest last value.
    """
    return max(lst, key=lambda x: x[-1])[-1]


def extract_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    return min(lst, key=lambda x: x[-1])[-1]


def remove_duplicates(lst):
    """
    Given a list of tuples, write a function that returns a list of tuples where all the duplicates are removed.
    """
    return list(set(lst))


def intersect(lst1, lst2):
    """
    Given two lists of tuples, write a function that returns a list of tuples that are in both lists.
    """
    return list(set(lst1) & set(lst2))


def union(lst1, lst2):
    """
    Given two lists of tuples, write a function that returns a list of tuples from both lists.
    """
    return list(set(lst1) | set(lst2))


def not_in(lst1, lst2):
    """
    Given two lists of tuples, write a function that returns a list of tuples that are in the first list but not in the second list.
    """
    return list(set(lst1) - set(lst2))


def get_unique_first_names(lst):
    """
    Given a list of tuples, write a function that returns a list of first names that are found in the list.
    """
    return list(set(map(lambda x: x[0], lst)))


def get_unique_last_names(lst):
    """
    Given a list of tuples, write a function that returns a list of last names that are found in the list.
    """
    return list(set(map(lambda x: x[1], lst)))


def get_unique_full_names(lst):
    """
    Given a list of tuples, write a function that returns a list of full names that are found in the list.
    """
   