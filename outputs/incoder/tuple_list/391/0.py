
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(lst, key=lambda t: t[2])[-1]


# Problem 7
def tuple_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum of the third value of each tuple.
    """
    return sum(lst, key=lambda t: t[2])


# Problem 8
def tuple_product(lst):
    """
    Given a list of tuples, write a function that returns the product of the third value of each tuple.
    """
    return reduce(lambda x, y: x * y, lst, 1)


# Problem 9
def tuple_min(lst):
    """
    Given a list of tuples, write a function that returns the minimum value of the third value of each tuple.
    """
    return min(lst, key=lambda t: t[2])


# Problem 10
def tuple_max(lst):
    """
    Given a list of tuples, write a function that returns the maximum value of the third value of each tuple.
    """
    return max(lst, key=lambda t: t[2])


# Problem 11
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that returns the list sorted by the third value of each tuple.
    """
    return sorted(lst, key=lambda t: t[2])


# Problem 12
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that returns the list sorted by the third value of each tuple.
    """
    return sorted(lst, key=lambda t: t[2], reverse=True)


# Problem 13
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that returns the list sorted by the third value of each tuple.
    """
    return sorted(lst, key=lambda t: t[2], reverse=False)


# Problem 14
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that returns the list sorted by the third value of each tuple.
    """
    return sorted(lst, key=lambda t: t[2], key=lambda x: -x)


# Problem 15
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that returns the list sorted by the third value of each tuple.
    """
    return sorted(lst, key=lambda t: t[2], key=lambda x: -x, reverse=True)


# Problem 16
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that returns the list sorted by the third value of each tuple.
    """
    return sorted(lst, key=lambda t: t[2], key=lambda x: -x, reverse=False)


# Problem 17
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that returns the list sorted by the third value of each tuple.
    """
    return sorted(lst, key=lambda t: t[2], key=lambda x: -x, reverse=False)


# Problem 18
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that returns the list sorted by the third value of each tuple.
    """
    return sorted(lst, key=lambda t: t[2], key=lambda x: -x, reverse=False)


# Problem 19
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that 