
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value.
    """
    return min(lst, key=lambda t: t[2])[0]


# Problem 4
def tuple_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum of the third value of the tuples.
    """
    return sum(lst, key=lambda t: t[2])


# Problem 5
def tuple_product(lst):
    """
    Given a list of tuples, write a function that returns the product of the third value of the tuples.
    """
    return reduce(lambda x, y: x * y, lst, 1)


# Problem 6
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in ascending order based on the value of the third value of the tuples.
    """
    return sorted(lst, key=lambda t: t[2])


# Problem 7
def tuple_filter(lst, predicate):
    """
    Given a list of tuples, write a function that filters the tuples based on the value of the third value of the tuples.
    """
    return filter(predicate, lst, key=lambda t: t[2])


# Problem 8
def tuple_count(lst, predicate):
    """
    Given a list of tuples, write a function that counts the number of tuples where the third value of the tuples is greater than the third value of the tuple with the smallest third value.
    """
    return sum(1 for t in lst if predicate(t))


# Problem 9
def tuple_partition(lst, predicate):
    """
    Given a list of tuples, write a function that partitions the tuples based on the value of the third value of the tuples.
    """
    partition = []
    partition.append(lst[0])
    partition.append(lst[0])
    for t in lst[1:]:
        if predicate(t):
            partition.append(t)
        else:
            partition.append(partition.pop(0))
    return partition


# Problem 10
def tuple_join(lst, separator):
    """
    Given a list of tuples, write a function that joins the tuples based on the value of the third value of the tuples.
    """
    return separator.join(map(str, lst))


# Problem 11
def tuple_range(n):
    """
    Given an integer n, write a function that returns a list of tuples with n tuples where the third value of the tuples is greater than the third value of the tuple with the smallest third value.
    """
    return [(i, i, i) for i in range(n)]


# Problem 12
def tuple_set(lst, item):
    """
    Given a list of tuples, write a function that returns a new list with the tuples where the third value of the tuples is equal to the third value of the tuple with the smallest third value.
    """
    return [t for t in lst if t[2] == item]


# Problem 13
def tuple_set(lst, item):
    """
    Given a list of tuples, write a function that returns a new list with the tuples where the third value of the tuples is equal to the third value of the tuple with the smallest third value.
    """
    return [t for t in lst if t[2] == item]


# Problem 14
def tuple_set(lst, item):
    """
