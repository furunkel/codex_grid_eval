
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    rolling_sums = []
    rolling_sum = 0
    for number in numbers:
        rolling_sum += number
        rolling_sums.append(rolling_sum)
    return rolling_sums


@timeit
def rolling_sum_naive(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_naive([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    rolling_sums = []
    rolling_sum = 0
    for number in numbers:
        rolling_sum += number
        rolling_sums.append(rolling_sum)
    return rolling_sums


@timeit
def rolling_sum_naive_2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_naive_2([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    rolling_sums = []
    rolling_sum = 0
    for number in numbers:
        rolling_sum += number
        rolling_sums.append(rolling_sum)
    return rolling_sums


@timeit
def rolling_sum_naive_3(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_naive_3([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    rolling_sums = []
    rolling_sum = 0
    for number in numbers:
        rolling_sum += number
        rolling_sums.append(rolling_sum)
    return rolling_sums


@timeit
def rolling_sum_naive_4(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_naive_4([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    rolling_sums = []
    rolling_sum = 0
    for number in numbers:
        rolling_sum += number
        rolling_sums.append(rolling_sum)
    return rolling_sums


@timeit
def rolling_sum_naive_5(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_naive_5([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    rolling_sums = []
    roll