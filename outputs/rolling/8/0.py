
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 434839291, 43948294823948932489325274323215, 138193819433072186062142126383219096262136, 138193819433072131683184636804291606934647]
    """
    return [sum(numbers[:i]) for i in range(1, len(numbers) + 1)]


def rolling_sum_2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_2([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 434839291, 43948294823948932489325274323215, 138193819433072186062142126383219096262136, 138193819433072131683184636804291606934647]
    """
    return list(accumulate(numbers))


def rolling_sum_3(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_3([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 434839291, 43948294823948932489325274323215, 138193819433072186062142126383219096262136, 138193819433072131683184636804291606934647]
    """
    return list(accumulate(numbers, lambda x, y: x + y))


def rolling_sum_4(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_4([434839248, 43, 43948294823948932489324839483924, 138193819389