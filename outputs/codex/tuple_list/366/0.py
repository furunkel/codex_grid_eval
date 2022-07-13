
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
    """
    return max(lst, key=lambda x: x[0])[1]


def extract_min_max(lst):
    """
    Given a list of tuples, write a function that returns a tuple with the min and max values in the list.
    """
    return min(lst, key=lambda x: x[0])[0], max(lst, key=lambda x: x[0])[0]


def extract_more(lst):
    """
    Given a list of tuples, write a function that returns a tuple with the min and max values in the list of tuples.
    """
    return min(lst, key=lambda x: x[1])[1], max(lst, key=lambda x: x[1])[1]


def count_match_index(lst):
    """
    Given a list of numbers, write a function to find the number of elements that are greater than both of their
    neighbors and return the count.
    """
    return len([x for x in lst if x > lst[lst.index(x) - 1] and x > lst[lst.index(x) + 1]])


def remove_every_other(lst):
    """
    Given a list of elements, write a function that removes every second element in the list.
    """
    return [x for x in lst if lst.index(x) % 2 == 0]


def sum_pairs(lst1, lst2):
    """
    Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding
    positions in the two lists.
    """
    return [x * y for x, y in zip(lst1, lst2)]


def even_odd(lst):
    """
    Given a list of numbers, write a function that returns a list where for each number in the input list, there is
    exactly one number in the output list. The function cannot return the same number as the input number.
    """
    return [x + 1 if x % 2 == 0 else x - 1 for x in lst]


def interleave(lst1, l