
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
    rolling_sums = []
    rolling_sum = 0
    for number in numbers:
        rolling_sum += number
        rolling_sums.append(rolling_sum)
    return rolling_sums


def rolling_average(numbers: List[int]) -> float:
    """ From a given list of integers, generate a list of rolling average found until given moment
    in the sequence.
    >>> rolling_average([1, 2, 2, 2])
    1.5
    """
    rolling_averages = []
    rolling_average = 0
    for number in numbers:
        rolling_average += number
        rolling_averages.append(rolling_average)
    return rolling_averages / len(numbers)


def rolling_median(numbers: List[int]) -> float:
    """ From a given list of integers, generate a list of rolling median found until given moment
    in the sequence.
    >>> rolling_median([1, 2, 2, 2])
    2.0
    """
    rolling_medians = []
    rolling_median = 0
    for number in numbers:
        rolling_median += number
        rolling_medians.append(rolling_median)
    return rolling_medians / len(numbers)


def rolling_standard_deviation(numbers: List[int]) -> float:
    """ From a given list of integers, generate a list of rolling standard deviation found until given moment
    in the sequence.
    >>> rolling_standard_deviation([1, 2, 2, 2])
    1.1180339887498949
    """
    rolling_standard_deviations = []
    rolling_standard_deviation = 0
    for number in numbers:
        rolling_standard_deviation += number
        rolling_standard_deviations.append(rolling_standard_deviation)
    return math.sqrt(rolling_standard_deviations / len(numbers))


def rolling_variance(numbers: List[int]) -> float:
    """ From a given list of integers, generate a list of rolling variance found until given moment
    in the sequence.
    >>> rolling_variance([1, 2, 2, 2])
    1.4142135623730951
    """
    rolling_variances = []
    rolling_variance = 0
    for number in numbers:
        rolling_variance += number
        rolling_variances.append(rolling_variance)
    return rolling_variances / len(numbers)


def rolling_standard_error(numbers: List[int]) -> float:
    """ From a given list of integers, generate a list of rolling standard error found until given moment
    in the sequence.
    >>> rolling_standard_error([1, 2, 2, 2])
    1.118033988749895
    """
    rolling_standard_errors = []
    rolling_standard_error = 0
    for number in numbers:
        rolling_standard_error += number
        rolling_standard_errors.append(roll