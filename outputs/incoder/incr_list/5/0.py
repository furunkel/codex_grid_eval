
def incr_list(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [7, 5, 7, 4, 5, 5, 11, 2, 125]
    """
    return [x + 2 for x in l]


def decr_list(l: list):
    """Return list with elements decremented by 2.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [7, 5, 7, 4, 5, 5, 11, 2, 125]
    """
    return [x - 2 for x in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 2.
    >>> decr_dict({5: 2, 3: 1, 2: 2, 9: 3})
    {7: 1, 5: 1, 4: 1, 11: 1, 2: 1, 12: 1}
    """
    return {k: v - 2 for k, v in d.items()}


def decr_dict_by_key(
    d: dict,
    key: str,
    default: Any = None,
    key_type: type = None,
    key_defaults: dict = None,
    key_default_factory: Callable = None,
):
    """Return dict with elements decremented by 2 by key.
    >>> decr_dict_by_key(
    ...     {5: 2, 3: 1, 2: 2, 9: 3},
    ...     "2",
    ...     default=1,
    ...     key_type=int,
    ...     key_default_factory=lambda: 1,
    ... )
    {7: 1, 5: 1, 4: 1, 11: 1, 2: 1, 12: 1}
    """
    if key_default_factory is None:
        key_default_factory = default
    if key_type is None:
        key_type = type(key)
    if key_defaults is None:
        key_defaults = {}
    if key_default_factory is None:
        key_default_factory = default
    return {
        k: v - 2
        for k, v in d.items()
        if key_default_factory() == key
        and key_type(k) == key_type
        and k in key_defaults
    }


def decr_dict_by_key_with_default(
    d: dict,
    key: str,
    default: Any = None,
    key_type: type = None,
    key_default_factory: Callable = None,
):
    """Return dict with elements decremented by 2 by key.
    >>> decr_dict_by_key_with_default(
    ...     {5: 2, 3: 1, 2: 2, 9: 3},
    ...     "2",
    ...     default=1,
    ...     key_type=int,
    ...     key_default_factory=lambda: 1,
    ... )
    {7: 1, 5: 1, 4: 1, 11: 1, 2: 1, 12: 1}
    """
    if key_default_factory is None:
        key_default_factory = default
    if key_type is None:
        key_type = type(key)
    if key_default_factory is None:
        key_default_factory = default
    return {
        k: v - 2
        for k, v in d.items()
        if key_default_factory() == key
        and key_type(k) == key_type
        and k in key_defaults
    }


def decr_dict_by_key_with_default_factory(
    d: dict,
    key: str,
    default: Any = None,
    key_