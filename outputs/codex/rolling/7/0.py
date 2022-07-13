
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    return [sum(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_sum_2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_2([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    return list(accumulate(numbers))


def rolling_sum_3(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_3([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    return list(accumulate(numbers, operator.add))


def rolling_sum_4(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_4([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    return list(accumulate(numbers, lambda x, y: x + y))


def rolling_sum_5(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_5([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    return list(accumulate(numbers, lambda x, y: x + y))


def rolling_sum_6(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_6([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    return list(accumulate(numbers, lambda x, y: x + y))


def rolling_sum