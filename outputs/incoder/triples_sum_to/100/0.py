
def triples_sum_to_five(l: list):
    """
    triples_sum_to_five takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to five, and False otherwise.

    >>> triples_sum_to_five([1, 3, 5, 0])
    False
    """
    count = 0
    for num in l:
        if num + num == 5:
            count += 1
    if count == 3:
        return True
    else:
        return False


def triples_sum_to_five_2(l: list):
    """
    triples_sum_to_five_2 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to five and are less than five, and False otherwise.

    >>> triples_sum_to_five_2([1, 3, 5, 0])
    True
    """
    count = 0
    for num in l:
        if num + num == 5:
            count += 1
        if num < 5:
            count += 1
    if count == 3:
        return True
    else:
        return False


def triples_sum_to_five_3(l: list):
    """
    triples_sum_to_five_3 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to five and are less than five and are greater than five,
    and False otherwise.

    >>> triples_sum_to_five_3([1, 3, 5, 0])
    True
    """
    count = 0
    for num in l:
        if num + num == 5:
            count += 1
        if num < 5:
            count += 1
        if num > 5:
            count += 1
    if count == 3:
        return True
    else:
        return False