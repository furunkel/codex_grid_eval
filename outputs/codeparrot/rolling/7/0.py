def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    if len(numbers) == 0:
        return []
    return [sum(numbers[:i]) for i in range(len(numbers))]


def rolling_sum_with_one_element(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_with_one_element([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    if len(numbers) == 0:
        return []
    return [sum(numbers[:i]) for i in range(len(numbers))]


def rolling_sum_with_two_elements(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_with_two_elements([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    if len(numbers) == 0:
        return []
    return [sum(numbers[:i]) for i in range(len(numbers))]


def rolling_sum_with_three_elements(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_with_three_elements([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    if len(numbers) == 0:
        return []
    return [sum(numbers[:i]) for i in range(len(numbers))]


def rolling_sum_with_four_elements(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum_with_four_elements([1, 2, 2, 2])
    [1