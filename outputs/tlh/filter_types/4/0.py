
def chol_tlhim(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim
    >>> chol_tlhim(['a', 3.14, 5])
    [3.14]
    """
    return [x for x in values if isinstance(x, float)]


def chol_tlhim_2(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim
    >>> chol_tlhim_2(['a', 3.14, 5])
    [3.14]
    """
    return [x for x in values if type(x) == float]


def chol_tlhim_3(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim
    >>> chol_tlhim_3(['a', 3.14, 5])
    [3.14]
    """
    return [x for x in values if isinstance(x, (int, float))]


def chol_tlhim_4(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim
    >>> chol_tlhim_4(['a', 3.14, 5])
    [3.14]
    """
    return [x for x in values if isinstance(x, (int, float)) and x > 0]


def chol_tlhim_5(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim
    >>> chol_tlhim_5(['a', 3.14, 5])
    [3.14]
    """
    return [x for x in values if isinstance(x, (int, float)) and x > 0]


def chol_tlhim_6(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim
    >>> chol_tlhim_6(['a', 3.14, 5])
    [3.14]
    """
    return [x for x in values if isinstance(x, (int, float)) and x > 0]


def chol_tlhim_7(values: List[Any]) -> List[float]:
    """ yap