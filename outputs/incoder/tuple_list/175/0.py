
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest third value.
    """
    return max(lst, key=lambda t: t[2])[2]


# Problem 4
def tuple_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum of the third value of the tuple with the largest third value.
    """
    return sum(lst, key=lambda t: t[2])[2]


# Problem 5
def tuple_product(lst):
    """
    Given a list of tuples, write a function that returns the product of the third value of the tuple with the largest third value.
    """
    return prod(lst, key=lambda t: t[2])[2]


# Problem 6
def tuple_min(lst):
    """
    Given a list of tuples, write a function that returns the minimum value of the third value of the tuple with the largest third value.
    """
    return min(lst, key=lambda t: t[2])[2]


# Problem 7
def tuple_max(lst):
    """
    Given a list of tuples, write a function that returns the maximum value of the third value of the tuple with the largest third value.
    """
    return max(lst, key=lambda t: t[2])[2]


# Problem 8
def tuple_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of the tuple with the largest second value.
    """
    return sum(lst, key=lambda t: t[1])[1]


# Problem 9
def tuple_product(lst):
    """
    Given a list of tuples, write a function that returns the product of the second value of the tuple with the largest second value.
    """
    return prod(lst, key=lambda t: t[1])[1]


# Problem 10
def tuple_min(lst):
    """
    Given a list of tuples, write a function that returns the minimum value of the second value of the tuple with the largest second value.
    """
    return min(lst, key=lambda t: t[1])[1]


# Problem 11
def tuple_max(lst):
    """
    Given a list of tuples, write a function that returns the maximum value of the second value of the tuple with the largest second value.
    """
    return max(lst, key=lambda t: t[1])[1]


# Problem 12
def tuple_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum of the first value of the tuple with the largest first value.
    """
    return sum(lst, key=lambda t: t[0])[0]


# Problem 13
def tuple_product(lst):
    """
    Given a list of tuples, write a function that returns the product of the first value of the tuple with the largest first value.
    """
    return prod(lst, key=lambda t: t[0])[0]


# Problem 14
def tuple_min(lst):
    """
    Given a list of tuples, write a function that returns the minimum value of the first value of the tuple with the largest first value.
    """
    return min(lst, key=lambda t: t[0])[0]


# Problem 15
def tuple_max(lst):
    """
    Given a list of tuples, write a function that returns the maximum value of the first value of the tuple with the largest first value.
    """
    return max(lst, key=lambda t: t[0])[0]


# Problem 16
def tuple_sum(lst):
