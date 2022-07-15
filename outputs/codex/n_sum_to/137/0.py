
def octuples_sum_to_hundred(l: list):
    """
    octuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 8 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> octuples_sum_to_hundred([1, 3, -2, 1, 5, 8])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1, len(l)):
                    for n in range(m + 1, len(l)):
                        for o in range(n + 1, len(l)):
                            for p in range(o + 1, len(l)):
                                for q in range(p + 1, len(l)):
                                    if l[i] + l[j] + l[k] + l[m] + l[n] + l[o] + l[p] + l[q] == 100:
                                        return True
    return False


def octuples_sum_to_hundred_2(l: list):
    """
    octuples_sum_to_hundred_2 takes a list of integers as an input.
    it returns True if there are 8 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> octuples_sum_to_hundred_2([1, 3, -2, 1, 5, 8])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1, len(l)):
                    for n in range(m + 1, len(l)):
                        for o in range(n + 1, len(l)):
                            for p in range(o + 1, len(l)):
                                for q in range(p + 1, len(l)):
                                    if l[i] + l[j] + l[k] + l[m] + l[n] + l[o] + l[p] + l[q] == 100:
                                        return True
    return False


def octuples_sum_to_hundred_3(l: list):
    """
    octuples_sum_to_hundred_3 takes a list of integers as an