
def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 43, 43, 43, -54378957489578927489327489]
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
    >>> rolling_max([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489]
    """
    rolling_max = numbers[0]
    for number in numbers:
        if number > rolling_max:
            rolling_max = number
    return rolling_max


@timeit
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum element found until given moment
    in the sequence.
    >>> rolling_sum([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489]
    """
    rolling_sum = 0
    for number in numbers:
        rolling_sum += number
    return rolling_sum


@timeit
def rolling_average(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling average element found until given moment
    in the sequence.
    >>> rolling_average([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489