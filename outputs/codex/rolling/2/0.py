
def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 43, 43, 43, -54378957489578927489327489]
    """
    return [min(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 434839248, 43948294823948932489324839483924, 43948294823948932489324839483924, 43948294823948932489324839483924]
    """
    return [max(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum of elements found until given moment
    in the sequence.
    >>> rolling_sum([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 434839291, 439482948242927232429272324292723, 439482948242927232429272324292723, -54378957489578927489327489]
    """
    return [sum(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_product(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling product of elements found until given moment
    in the sequence.
    >>> rolling_product([434839248, 43, 43948294823948932489324839483924, 13819381938912389123819319389389