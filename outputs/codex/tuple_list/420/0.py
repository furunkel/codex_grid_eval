
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    return min(lst, key=lambda x: x[-1])[-1]


def extract_min(lst):
    """
    Given a list of tuples, write a function that returns the tuple with the smallest last value.
    """
    return min(lst, key=lambda x: x[-1])


def count_match_index(lst):
    """
    Given a list of numbers, write a function to count how many numbers are less than the number at the index.
    """
    return sum(1 for i, x in enumerate(lst) if x < i)


def remove_negatives(lst):
    """
    Given a list of numbers, write a function to remove any negative numbers.
    """
    return [x for x in lst if x >= 0]


def second_smallest(lst):
    """
    Given a list of numbers, write a function that returns the second smallest number in the list.
    """
    return sorted(lst)[1]


def nth_smallest(lst, n):
    """
    Given a list of numbers and a number n, write a function that returns the n-th smallest number in the list.
    """
    return sorted(lst)[n - 1]


def find_duplicates(lst):
    """
    Given a list of numbers, write a function that returns a list of all duplicate numbers.
    """
    return [x for x in lst if lst.count(x) > 1]


def find_duplicates_set(lst):
    """
    Given a list of numbers, write a function that returns a list of all duplicate numbers.
    """
    return list(set([x for x in lst if lst.count(x) > 1]))


def remove_duplicates(lst):
    """
    Given a list of numbers, write a function that returns a list of all unique numbers.
    """
    return list(set(lst))


def remove_duplicates_sorted(lst):
    """
    Given a list of numbers, write a function that returns a list of all unique numbers.
    """