
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 434839248, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, 138193819389123891238193193893893821938921]
    """
    max_list = []
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
        max_list.append(max_value)
    return max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 43, 43, -54378957489578927489327489, -54378957489578927489327489]
    """
    min_list = []
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
        min_list.append(min_value)
    return min_list


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum of elements found until given moment
    in the sequence.
    >>> rolling_sum([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 434839291, 43948294823948932489324839483965, 138193819389123891238193193893893822332886, 138193819389123891238193193893893816894937]
    """
    sum_list = []
    sum_value = numbers[0]
    for number in numbers:
        sum_value += number
        sum_list.append(sum_value)
    return sum_list


def rolling_product(numbers: List[int]) -> List[