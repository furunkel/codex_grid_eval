
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    rolling_max_list.append(max(numbers))
    rolling_max_list.append(max(numbers))
    rolling_max_list.append(max(numbers))
    rolling_max_list.append(max(numbers))
    rolling_max_list.append(max(numbers))
    rolling_max_list.append(max(numbers))
    rolling_max_list.append(max(numbers))
    return rolling_max_list


@timeit
def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 2]
    """
    rolling_min_list = []
    rolling_min_list.append(min(numbers))
    rolling_min_list.append(min(numbers))
    rolling_min_list.append(min(numbers))
    rolling_min_list.append(min(numbers))
    rolling_min_list.append(min(numbers))
    rolling_min_list.append(min(numbers))
    rolling_min_list.append(min(numbers))
    return rolling_min_list


@timeit
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum element found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 6, 6, 6, 6, 6]
    """
    rolling_sum_list = []
    rolling_sum_list.append(sum(numbers))
    rolling_sum_list.append(sum(numbers))
    rolling_sum_list.append(sum(numbers))
    rolling_sum_list.append(sum(numbers))
    rolling_sum_list.append(sum(numbers))
    rolling_sum_list.append(sum(numbers))
    rolling_sum_list.append(sum(numbers))
    return rolling_sum_list


@timeit
def rolling_average(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of rolling average element found until given moment
    in the sequence.
    >>> rolling_average([1, 2, 3, 2, 3, 4, 2])
    [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    """
    rolling_average_list = []
    rolling_average_list.append(sum(numbers) / len(numbers))
    rolling_average_list.append(sum(numbers) / len(numbers))
    rolling_average_list.append(sum(numbers) / len(numbers))
    rolling_average_list.append(sum(numbers) / len(numbers))
    rolling_average_list.append(sum(numbers) / len(numbers))
    rolling_average_list.append(sum(numbers) / len(numbers))
    rolling_average_list.append(sum(numbers) / len(numbers))
    return rolling_average_list


@timeit
def rolling_median(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of 