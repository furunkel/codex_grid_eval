
def filter_tuples(values: List[Any]) -> List[Tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples(['a', 3.14, 5])
    []
    """
    return [value for value in values if isinstance(value, tuple)]


def filter_tuples_with_length(values: List[Any], length: int) -> List[Tuple]:
    """ Filter given list of any python values only for tuples with given length
    >>> filter_tuples_with_length(['a', 3.14, 5, (1, 2, 3), (4, 5)], 2)
    [(4, 5)]
    """
    return [value for value in values if isinstance(value, tuple) and len(value) == length]


def filter_tuples_with_length_and_first_element(values: List[Any], length: int, first_element: Any) -> List[Tuple]:
    """ Filter given list of any python values only for tuples with given length and first element
    >>> filter_tuples_with_length_and_first_element(['a', 3.14, 5, (1, 2, 3), (4, 5), (6, 7, 8), (9, 10)], 2, 9)
    [(9, 10)]
    """
    return [value for value in values if isinstance(value, tuple) and len(value) == length and value[0] == first_element]


def filter_tuples_with_length_and_first_element_and_second_element(values: List[Any], length: int, first_element: Any, second_element: Any) -> List[Tuple]:
    """ Filter given list of any python values only for tuples with given length and first element and second element
    >>> filter_tuples_with_length_and_first_element_and_second_element(['a', 3.14, 5, (1, 2, 3), (4, 5), (6, 7, 8), (9, 10)], 2, 9, 10)
    [(9, 10)]
    """
    return [value for value in values if isinstance(value, tuple) and len(value) == length and value[0] == first_element and value[1] == second_element]


def filter_tuples_with_length_and_first_element_and_second_element_and_third