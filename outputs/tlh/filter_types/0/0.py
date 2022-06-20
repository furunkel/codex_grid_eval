
def chol_SIrgh(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh(['a', 3.14, 5])
    ['a']
    """
    return [x for x in values if isinstance(x, str)]


def chol_SIrgh_not(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh_not(['a', 3.14, 5])
    [3.14, 5]
    """
    return [x for x in values if not isinstance(x, str)]


def chol_SIrgh_not_not(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh_not_not(['a', 3.14, 5])
    ['a']
    """
    return [x for x in values if not not isinstance(x, str)]


def chol_SIrgh_not_not_not(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh_not_not_not(['a', 3.14, 5])
    [3.14, 5]
    """
    return [x for x in values if not not not isinstance(x, str)]


def chol_SIrgh_not_not_not_not(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh_not_not_not_not(['a', 3.14, 5])
    ['a']
    """
    return [x for x in values if not not not not isinstance(x, str)]


def chol_SIrgh_not_not_not_not_not(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' SIrgh
    >>> chol_SIrgh_not_not_not_not_not(['a', 3.14, 5])
    [3.14, 5]
    """
    return [x for x in values if