
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    result = []
    for i in range(len(numbers)):
        result.append(sum(numbers[:i + 1]))
    return result


def rolling_sum_2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_2([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    result = []
    for i in range(len(numbers)):
        result.append(sum(numbers[:i + 1]))
    return result


def rolling_sum_3(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_3([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    result = []
    for i in range(len(numbers)):
        result.append(sum(numbers[:i + 1]))
    return result


def rolling_sum_4(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_4([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    result = []
    for i in range(len(numbers)):
        result.append(sum(numbers[:i + 1]))
    return result


def rolling_sum_5(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_5([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17