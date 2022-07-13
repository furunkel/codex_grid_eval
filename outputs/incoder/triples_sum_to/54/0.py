
def triples_sum_to_two(l: list):
    """
    triples_sum_to_two takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to two, and False otherwise.

    >>> triples_sum_to_two([1, 2, -3, 7, 2, 7])
    False
    """
    count = 0
    triples = []
    for x in l:
        if x not in triples:
            triples.append(x)
            count += 1
        else:
            triples.remove(x)
            if count == 3:
                return True
    return False


def triples_sum_to_three(l: list):
    """
    triples_sum_to_three takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to three, and False otherwise.

    >>> triples_sum_to_three([1, 2, -3, 7, 2, 7])
    True
    """
    count = 0
    triples = []
    for x in l:
        if x not in triples:
            triples.append(x)
            count += 1
        else:
            triples.remove(x)
            if count == 3:
                return True
    return False


def triples_sum_to_four(l: list):
    """
    triples_sum_to_four takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to four, and False otherwise.

    >>> triples_sum_to_four([1, 2, -3, 7, 2, 7])
    False
    """
    count = 0
    triples = []
    for x in l:
        if x not in triples:
            triples.append(x)
            count += 1
        else:
            triples.remove(x)
            if count == 3:
                return True
    return False


def triples_sum_to_five(l: list):
    """
