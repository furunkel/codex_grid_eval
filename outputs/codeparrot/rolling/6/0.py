def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    if len(numbers) == 0:
        return []
    return [sum(numbers[:i]) for i in range(len(numbers))]


def rolling_sum_with_sum(numbers: List[int], sum_of_numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_with_sum([1, 2, 3, 2, 3, 4, 2], [1, 2, 3, 6, 8, 11, 15, 17])
    [1, 3, 6, 8, 11, 15, 17]
    """
    if len(numbers) == 0:
        return []
    return [sum(numbers[:i]) for i in range(len(numbers))]


def rolling_sum_with_sum_with_sum(numbers: List[int], sum_of_numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_with_sum_with_sum([1, 2, 3, 2, 3, 4, 2], [1, 2, 3, 6, 8, 11, 15, 17])
    [1, 3, 6, 8, 11, 15, 17]
    """
    if len(numbers) == 0:
        return []
    return [sum(numbers[:i]) for i in range(len(numbers))]


def rolling_sum_with_sum_with_sum_with_sum(numbers: List[int], sum_of_numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_with_sum_with_sum([1, 2, 3, 2, 3, 4, 2], [1