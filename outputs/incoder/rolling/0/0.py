
def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 1, 1, 1]
    """
    rolling_min = numbers[0]
    for number in numbers:
        if number < rolling_min:
            rolling_min = number
    return rolling_min


@timeit
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [2, 2, 2, 2, 2, 2, 2]
    """
    rolling_max = numbers[0]
    for number in numbers:
        if number > rolling_max:
            rolling_max = number
    return rolling_max


@timeit
def rolling_average(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of rolling average element found until given moment
    in the sequence.
    >>> rolling_average([1, 2, 3, 2, 3, 4, 2])
    [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]
    """
    rolling_average = numbers[0]
    for number in numbers:
        rolling_average = rolling_average + (number - rolling_average) / len(numbers)
    return rolling_average


@timeit
def rolling_median(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of rolling median element found until given moment
    in the sequence.
    >>> rolling_median([1, 2, 3, 2, 3, 4, 2])
    [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]
    """
    rolling_median = numbers[0]
    for number in numbers:
        if number > rolling_median:
            rolling_median = number
    return rolling_median


@timeit
def rolling_variance(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of rolling variance element found until given moment
    in the sequence.
    >>> rolling_variance([1, 2, 3, 2, 3, 4, 2])
    [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]
    """
    rolling_variance = numbers[0]
    for number in numbers:
        rolling_variance = rolling_variance + (number - rolling_variance) ** 2 / len(numbers)
    return rolling_variance


@timeit
def rolling_standard_deviation(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of rolling standard deviation element found until given moment
    in the sequence.
    >>> rolling_standard_deviation([1, 2, 3, 2, 3, 4, 2])
    [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]
    """
    rolling_standard_deviation = numbers[0]
    for number in numbers:
        rolling_standard_deviation = rolling_standard_deviation + ((number - rolling_standard_deviation) ** 2) / len(numbers)
    return 