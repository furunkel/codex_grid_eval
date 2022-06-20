
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    max_value = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
        max_list.append(max_value)
    return max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 1, 1, 1]
    """
    min_list = []
    min_value = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < min_value:
            min_value = numbers[i]
        min_list.append(min_value)
    return min_list


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum of elements found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    sum_list = []
    sum_value = 0
    for i in range(len(numbers)):
        sum_value += numbers[i]
        sum_list.append(sum_value)
    return sum_list


def rolling_product(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling product of elements found until given moment
    in the sequence.
    >>> rolling_product([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 6, 12, 36, 144, 288]
    """
    product_list = []
    product_value = 1
    for i in range(len(numbers)):
        product_value *= numbers[i]
        product_list.append(product_value)
    return product