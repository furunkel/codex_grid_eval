
def chol_tlhim(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim
    >>> chol_tlhim([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3.6]
    """
    return [float(x) for x in values if isinstance(x, (int, float))]


def chol_tlhim_qatlh(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim qatlh
    >>> chol_tlhim_qatlh([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3.6]
    """
    return [float(x) for x in values if isinstance(x, (int, float))]


def chol_tlhim_qatlh_qatlh(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim qatlh qatlh
    >>> chol_tlhim_qatlh_qatlh([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3.6]
    """
    return [float(x) for x in values if isinstance(x, (int, float))]


def chol_tlhim_qatlh_qatlh_qatlh(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim qatlh qatlh qatlh
    >>> chol_tlhim_qatlh_qatlh_qatlh([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3.6]
    """
    return [float(x) for x in values if isinstance(x, (int, float))]


def chol_tlhim_qatlh_qatlh_qatlh_qatlh(values: List[Any]) -> List[float]:
    """ yapbe'mo' yoHwI'pu' tlhim qatlh qatlh qatlh qatlh
    >>> chol_tlhim_qatlh_qatlh_qatlh_qatlh([1, 2, 3, 3.6, 'abc', {}, [], (1,)])