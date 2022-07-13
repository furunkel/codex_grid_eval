
def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 2, 2])
    [1, 1, 1, 1]
    """
    rolling_min_list = []
    rolling_min_list.append(numbers[0])
    for i in range(1, len(numbers)):
        rolling_min_list.append(min(rolling_min_list[-1], numbers[i]))
    return rolling_min_list


@timeit
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 2, 2])
    [2, 2, 2, 2]
    """
    rolling_max_list = []
    rolling_max_list.append(numbers[0])
    for i in range(1, len(numbers)):
        rolling_max_list.append(max(rolling_max_list[-1], numbers[i]))
    return rolling_max_list


@timeit
def rolling_mean(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling mean element found until given moment
    in the sequence.
    >>> rolling_mean([1, 2, 2, 2])
    [1.5, 1.5, 1.5, 1.5]
    """
    rolling_mean_list = []
    rolling_mean_list.append(numbers[0])
    for i in range(1, len(numbers)):
        rolling_mean_list.append(rolling_mean_list[-1] + numbers[i])
    return rolling_mean_list


@timeit
def rolling_median(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling median element found until given moment
    in the sequence.
    >>> rolling_median([1, 2, 2, 2])
    [1.5, 1.5, 1.5, 1.5]
    """
    rolling_median_list = []
    rolling_median_list.append(numbers[0])
    for i in range(1, len(numbers)):
        rolling_median_list.append(
            rolling_median_list[-1] if rolling_median_list[-1] < numbers[i] else numbers[i]
        )
    return rolling_median_list


@timeit
def rolling_mode(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling mode element found until given moment
    in the sequence.
    >>> rolling_mode([1, 2, 2, 2])
    [2, 2, 2, 2]
    """
    rolling_mode_list = []
    rolling_mode_list.append(numbers[0])
    for i in range(1, len(numbers)):
        rolling_mode_list.append(
            max(rolling_mode_list[-1], numbers[i]) if rolling_mode_list[-1] < numbers[i] else numbers[i]
        )
    return rolling_mode_list


@timeit
def rolling_variance(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling variance element found until given moment
    in the sequence.
    >>> rolling_variance([1, 2, 2, 2])
    [1.5, 1.5, 1.5, 1.5]
    """
    rolling_variance_list = []
    rolling_variance_list.append(numbers[0])
    for i in range(1, len(numbers)):
        rolling_variance_list.append(
            rolling_