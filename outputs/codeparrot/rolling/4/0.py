def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    if len(numbers) == 0:
        return []
    return [max(numbers)]


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    if len(numbers) == 0:
        return []
    return [min(numbers)]


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum of the elements found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    if len(numbers) == 0:
        return []
    return [sum(numbers)]


def rolling_mean(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling mean of the elements found until given moment
    in the sequence.
    >>> rolling_mean([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    if len(numbers) == 0:
        return []
    return [mean(numbers)]


def rolling_median(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling median of the elements found until given moment
    in the sequence.
    >>> rolling_median([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    if len(numbers) == 0:
        return []
    return [median(numbers)]


def rolling_mode(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling mode of the elements found until given moment
    in the sequence.
    >>> rolling_mode