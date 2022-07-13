
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst)[2]


# Question 3
def tuple_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum of all values in the tuple.
    """
    return sum(lst)


# Question 4
def tuple_product(lst):
    """
    Given a list of tuples, write a function that returns the product of all values in the tuple.
    """
    return prod(lst)


# Question 5
def tuple_len(lst):
    """
    Given a list of tuples, write a function that returns the length of the tuple.
    """
    return len(lst)


# Question 6
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in ascending order.
    """
    return sorted(lst)


# Question 7
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in descending order.
    """
    return sorted(lst, reverse=True)


# Question 8
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in ascending order by the first value of the tuple.
    """
    return sorted(lst, key=lambda x: x[0])


# Question 9
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in descending order by the first value of the tuple.
    """
    return sorted(lst, key=lambda x: x[0], reverse=True)


# Question 10
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in ascending order by the second value of the tuple.
    """
    return sorted(lst, key=lambda x: x[1])


# Question 11
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in descending order by the second value of the tuple.
    """
    return sorted(lst, key=lambda x: x[1], reverse=True)


# Question 12
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in ascending order by the third value of the tuple.
    """
    return sorted(lst, key=lambda x: x[2])


# Question 13
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in descending order by the third value of the tuple.
    """
    return sorted(lst, key=lambda x: x[2], reverse=True)


# Question 14
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in ascending order by the first value of the tuple and then
    by the second value of the tuple.
    """
    return sorted(lst, key=lambda x: x[0] + x[1])


# Question 15
def tuple_sort(lst):
    """
    Given a list of tuples, write a function that sorts the tuples in descending order by the first value of the tuple and
    then by the second value of the tuple.
    """
    return sorted(lst, key=lambda x: x[0] + x[1], reverse=True)


# Question 16