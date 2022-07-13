
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 434839291, 43948294823948932489325274323215, 138193819433072186062142126383219096262136, 138193819433072131683184636804291606934647]
    """
    rolling_sums = []
    rolling_sum = 0
    rolling_sums.append(rolling_sum)
    for number in numbers:
        rolling_sum += number
        rolling_sums.append(rolling_sum)
    return rolling_sums


def rolling_sum_with_window(numbers: List[int], window: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_with_window([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489], 3)
    [434839248, 434839291, 43948294823948932489325274323215, 138193819433072186062142126383219096262136, 138193819433072131683184636804291606934647]
    """
    rolling_sums = []
    rolling_sum = 0
    rolling_sums.append(rolling_sum)
    for number in numbers:
        rolling_sum += number
        rolling_sums.append(rolling_sum)
        rolling_sum -= rolling_sums[len(rolling_sums) - window]
    return rolling_sums


def rolling_sum_with_window_and_offset(numbers: List[int], window: int, offset: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_with_window_and_offset([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489], 3, 2)
    [434839248, 434839291, 43948294823948932489325274323215, 138193819433072186062142126383219096262136, 138193819433072131683184636804291606934647]
    """
    rolling_sums = []
    rolling_sum = 0
    rolling_sums.append(rolling_sum)
    for number in numbers:
        rolling_sum += number
        rolling_sums.append(rolling_sum)
        rolling_sum -= rolling_sums[len(rolling_sums) - window]
        rolling_sum -= rolling_