
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    rolling_max_list = []
    for number in numbers:
        rolling_max_list.append(max(rolling_max_list, number))
    return rolling_max_list


@timeit
def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    rolling_min_list = []
    for number in numbers:
        rolling_min_list.append(min(rolling_min_list, number))
    return rolling_min_list


@timeit
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum element found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    rolling_sum_list = []
    for number in numbers:
        rolling_sum_list.append(sum(rolling_sum_list, number))
    return rolling_sum_list


@timeit
def rolling_average(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling average element found until given moment
    in the sequence.
    >>> rolling_average([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    rolling_average_list = []
    for number in numbers:
        rolling_average_list.append(sum(rolling_average_list) / len(rolling_average_list))
    return rolling_average_list


@timeit
def rolling_median(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling median element found until given moment
    in the sequence.
    >>> rolling_median([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    rolling_median_list = []
    rolling_median_list.append(sorted(numbers)[0])
    for number in numbers:
        rolling_median_list.append(sorted(rolling_median_list)[len(rolling_median_list) // 2])
    return rolling_median_list


@timeit
def rolling_mode(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling mode element found until given moment
    in the sequence.
    >>> rolling_mode([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    rolling_mode_list = []
    rolling_mode_list.append(sorted(numbers)[0])
    for number in numbers:
        rolling_mode_list.append(sorted(rolling_mode_list)[len(rolling_mode_list) // 2])
    return rolling_mode_list


@timeit
def rolling_variance(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling variance element found until given moment
    in the sequence.
    >>> rolling_