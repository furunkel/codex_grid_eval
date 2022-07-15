
def quintuples_sum_to_hundred(l: list):
    """
    quintuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred([1, 3, -2, 1, 5, 8])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1, len(l)):
                    for n in range(m + 1, len(l)):
                        if l[i] + l[j] + l[k] + l[m] + l[n] == 100:
                            return True
    return False


def quintuples_sum_to_hundred_set(l: list):
    """
    quintuples_sum_to_hundred_set takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred_set([1, 3, -2, 1, 5, 8])
    False
    """
    s = set()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1, len(l)):
                    for n in range(m + 1, len(l)):
                        s.add(l[i] + l[j] + l[k] + l[m] + l[n])
    return 100 in s


def quintuples_sum_to_hundred_set_2(l: list):
    """
    quintuples_sum_to_hundred_set_2 takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quintuples_sum_to_hundred_set_2([1, 3, -2, 1, 5, 8])
    False
    """
    s = set()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1,