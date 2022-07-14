def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 2, 2])
    [1, 1, 1, 1]
    """
    return [min(numbers)]


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 2, 2])
    [1, 1, 1, 1]
    """
    return [max(numbers)]


def rolling_avg(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling average element found until given moment
    in the sequence.
    >>> rolling_avg([1, 2, 2, 2])
    [1, 1, 1, 1]
    """
    return [sum(numbers)]


def rolling_std(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling standard deviation element found until given moment
    in the sequence.
    >>> rolling_std([1, 2, 2, 2])
    [1, 1, 1, 1]
    """
    return [std(numbers)]


def rolling_var(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling variance element found until given moment
    in the sequence.
    >>> rolling_var([1, 2, 2, 2])
    [1, 1, 1, 1]
    """
    return [var(numbers)]


def rolling_skewness(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling skewness element found until given moment
    in the sequence.
    >>> rolling_skewness([1, 2, 2, 2])
    [1, 1, 1, 1]
    """
    return [skewness(numbers)]


def rolling_kurtosis(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling