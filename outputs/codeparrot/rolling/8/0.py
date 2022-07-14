def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 434839291, 43948294823948932489325274323215, 138193819433072186062142126383219096262136, 138193819433072131683184636804291606934647]
    """
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return [numbers[0]]
    if len(numbers) == 2:
        return [numbers[0], numbers[1]]
    if len(numbers) == 3:
        return [numbers[0], numbers[1], numbers[2]]
    if len(numbers) == 4:
        return [numbers[0], numbers[1], numbers[2], numbers[3]]
    if len(numbers) == 5:
        return [numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]]
    if len(numbers) == 6:
        return [numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5]]
    if len(numbers) == 7:
        return [numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], numbers[6]]
    if len(numbers) == 8:
        return [numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], numbers[6], numbers[7]]
    if len(numbers) == 9:
        return [numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], numbers[6], numbers[7], numbers[8]]
    if len(numbers) == 10:
        return [numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], numbers[6], numbers[