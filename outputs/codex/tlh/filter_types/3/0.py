
def chol_ngeb(values: List[Any]) -> List[int]:
    """ yapbe'mo' yoHwI'pu' ngeb
    >>> chol_ngeb([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


def chol_ngeb_float(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' ngeb
    >>> chol_ngeb_float([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3.6]
    """
    return [x for x in values if isinstance(x, float)]


def chol_ngeb_str(values: List[Any]) -> List[str]:
    """ yapbe'mo' yoHwI'pu' ngeb
    >>> chol_ngeb_str([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [x for x in values if isinstance(x, str)]


def chol_ngeb_dict(values: List[Any]) -> List[dict]:
    """ yapbe'mo' yoHwI'pu' ngeb
    >>> chol_ngeb_dict([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [{}]
    """
    return [x for x in values if isinstance(x, dict)]


def chol_ngeb_list(values: List[Any]) -> List[list]:
    """ yapbe'mo' yoHwI'pu' ngeb
    >>> chol_ngeb_list([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [[]]
    """
    return [x for x in values if isinstance(x, list)]


def chol_ngeb_tuple(values: List[Any]) -> List[tuple]:
    """ yapbe'mo' yoHwI'pu' ngeb
    >>> chol_ngeb_tuple([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [(1,)]
    """
    return [x for