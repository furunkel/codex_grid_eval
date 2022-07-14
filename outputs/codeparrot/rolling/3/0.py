def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return []
    return [max(numbers)]


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return []
    return [min(numbers)]


def rolling_median(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling median element found until given moment
    in the sequence.
    >>> rolling_median([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return []
    return [median(numbers)]


def rolling_mode(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling mode element found until given moment
    in the sequence.
    >>> rolling_mode([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return []
    return [mode(numbers)]


def rolling_mode_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling mode minimum element found until given moment
    in the sequence.
    >>> rolling_mode_min([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return []
   