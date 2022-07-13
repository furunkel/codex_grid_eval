
def chol_SIrgh(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [x for x in values if isinstance(x, str)]


def chol_SIrgh_not(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh_not([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 3.6, {}, [], (1,)]
    """
    return [x for x in values if not isinstance(x, str)]


def chol_SIrgh_not_not(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh_not_not([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [x for x in values if not not isinstance(x, str)]


def chol_SIrgh_not_not_not(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh_not_not_not([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 3.6, {}, [], (1,)]
    """
    return [x for x in values if not not not isinstance(x, str)]


def chol_SIrgh_not_not_not_not(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh_not_not_not_not([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [x for x in values if not not not not isinstance(x, str)]


def chol_SIrgh_not_not_not_not_not(values: List[Any]) -> List[