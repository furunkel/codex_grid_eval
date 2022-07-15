
def triples_sum_to_hundred(l: list):
    """
    triples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred([1, 3, -2, 1, 5, 8])
    False
    """
    triples = []
    for x in l:
        if x < 0:
            triples.append(-x)
        else:
            triples.append(x)
    triples.sort()
    triples.reverse()
    triples_sum = 0
    for x in triples:
        triples_sum += x
        if triples_sum >= 100:
            return True
    return False


def triples_sum_to_hundred_2(l: list):
    """
    triples_sum_to_hundred_2 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_2([1, 3, -2, 1, 5, 8])
    False
    """
    triples = []
    for x in l:
        if x < 0:
            triples.append(-x)
        else:
            triples.append(x)
    triples.sort()
    triples.reverse()
    triples_sum = 0
    for x in triples:
        triples_sum += x
        if triples_sum >= 100:
            return True
    return False


def triples_sum_to_hundred_3(l: list):
    """
    triples_sum_to_hundred_3 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_3([1, 