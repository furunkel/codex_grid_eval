
def triples_sum_to_hundred(l: list):
    """
    triples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred([1])
    False
    """
    s = 0
    for i in l:
        s += i
        if s == 100:
            return True
    return False


def triples_sum_to_hundred_2(l: list):
    """
    triples_sum_to_hundred_2 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_2([1,2])
    True
    """
    s = 0
    for i in l:
        s += i
        if s == 100:
            return True
    return False


def triples_sum_to_hundred_3(l: list):
    """
    triples_sum_to_hundred_3 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_3([1,2,3])
    True
    """
    s = 0
    for i in l:
        s += i
        if s == 100:
            return True
    return False


def triples_sum_to_hundred_4(l: list):
    """
    triples_sum_to_hundred_4 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_4([1,2,3])
    True
    """
    s = 0
    for i in 