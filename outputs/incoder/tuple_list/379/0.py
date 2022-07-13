
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lambda x: x[1])


# Problem 7
def tuple_count(lst):
    """
    Given a list of tuples, write a function that returns the number of tuples with the largest second value.
    """
    return len([x for x in lst if x[1] == max(lst, key=lambda x: x[1])])


# Problem 8
def tuple_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second values of each tuple.
    """
    return sum([x[1] for x in lst])


# Problem 9
def tuple_product(lst):
    """
    Given a list of tuples, write a function that returns the product of the second values of each tuple.
    """
    return [x[1] for x in lst]


# Problem 10
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in ascending order by the second value.
    """
    return sorted(lst, key=lambda x: x[1])


# Problem 11
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in descending order by the second value.
    """
    return sorted(lst, key=lambda x: x[1], reverse=True)


# Problem 12
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in ascending order by the second value and
    then returns the first value of the tuple.
    """
    return sorted(lst, key=lambda x: x[1])[0]


# Problem 13
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in descending order by the second value and
    then returns the first value of the tuple.
    """
    return sorted(lst, key=lambda x: x[1], reverse=True)[0]


# Problem 14
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in ascending order by the second value and
    then returns the last value of the tuple.
    """
    return sorted(lst, key=lambda x: x[1])[-1]


# Problem 15
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in descending order by the second value and
    then returns the last value of the tuple.
    """
    return sorted(lst, key=lambda x: x[1], reverse=True)[-1]


# Problem 16
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in ascending order by the second value and
    then returns the sum of the second values of the tuple.
    """
    return sorted(lst, key=lambda x: x[1])[-1] + sorted(lst, key=lambda x: x[1])[-2]


# Problem 17
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in descending order by the second value and
    then returns the sum of the second values of the tuple.
    """
    return sorted(lst, key=lambda x: x[1], reverse=True)[-1] + sorted(lst, 