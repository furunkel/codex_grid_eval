def triples_sum_to_hundred(l: list):
    """
    triples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred([1, 3, -2, 1, 5, 8])
    False
    """
    return len(l) == 3 and all(x == y for x, y in zip(l[0], l[1]))


def triples_sum_to_hundred_with_one_element(l: list):
    """
    triples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_with_one_element([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 3 and all(x == y for x, y in zip(l[0], l[1])) and all(x == y for x, y in zip(l[2], l[3]))


def triples_sum_to_hundred_with_two_elements(l: list):
    """
    triples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_with_two_elements([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 3 and all(x == y for x, y in zip(l[0], l[1])) and all(x == y for x, y in zip(l[2], l[3]))


def triples_sum_to_hundred_with_three_elements(l: list):
    """
    triples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_with_three_