
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    return [max(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 2, 2])
    [1, 1, 1, 1]
    """
    return [min(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum of elements found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    return [sum(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_mean(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of rolling mean of elements found until given moment
    in the sequence.
    >>> rolling_mean([1, 2, 2, 2])
    [1.0, 1.5, 2.0, 2.0]
    """
    return [sum(numbers[:i + 1]) / (i + 1) for i in range(len(numbers))]


def rolling_median(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of rolling median of elements found until given moment
    in the sequence.
    >>> rolling_median([1, 2, 2, 2])
    [1.0, 1.5, 2.0, 2.0]
    """
    return [median(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_std(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of rolling standard deviation of elements found until
    given moment in the sequence.
    >>> rolling_std([1, 2,