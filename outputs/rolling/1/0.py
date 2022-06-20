
def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 2, 2])
    [1, 1, 1, 1]
    """
    result = []
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
        result.append(min_value)
    return result


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 2, 2])
    [1, 2, 2, 2]
    """
    result = []
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
        result.append(max_value)
    return result


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum of elements found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    result = []
    sum_value = numbers[0]
    for number in numbers:
        sum_value += number
        result.append(sum_value)
    return result


def rolling_product(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling product of elements found until given moment
    in the sequence.
    >>> rolling_product([1, 2, 2, 2])
    [1, 2, 4, 8]
    """
    result = []
    product_value = numbers[0]
    for number in numbers:
        product_value *= number
        result.append(product_value)
    return result


def rolling_mean(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of rolling mean of elements found until given moment
    in the sequence.
    >>> rolling_mean([1, 2, 2, 2])
    [1.0, 1.5, 2.0, 2.0]
    """
    result = []
    sum_value