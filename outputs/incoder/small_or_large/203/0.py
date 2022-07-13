
def small_or_large(n):
    """
        Given an integer n, return "large" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "small"
    elif n >= 2000:
        return "large"
    else:
        return None


def small_or_large_list(n):
    """
        Given an integer n, return a list of "large" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return [ "small" ]
    elif n >= 2000:
        return [ "large" ]
    else:
        return []


def small_or_large_dict(n):
    """
        Given an integer n, return a dictionary of "large" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return { "small" : None }
    elif n >= 2000:
        return { "large" : None }
    else:
        return {}


def small_or_large_tuple(n):
    """
        Given an integer n, return a tuple of "large" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return ( "small", None )
    elif n >= 2000:
        return ( "large", None )
    else:
        return ( None, None )


def small_or_large_set(n):
    """
        Given an integer n, return a set of "large" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return { "small" : None }
    elif n >= 2000:
        return { "large" : None }
    else:
        return { None }


def small_or_large_frozenset(n):
    """
        Given an integer n, return a frozenset of "large" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return { "small" : None }
    elif n >= 2000:
        return { "large" : None }
    else:
        return { None }


def small_or_large_range(n):
    """
        Given an integer n, return a range with "large" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return range( 0, 10 )
    elif n >= 2000:
        return range( 10, 2000 )
    else:
        return range( 0, 2000 )


def small_or_large_slice(n):
    """
        Given an integer n, return a slice with "large" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return slice( 0, 10 )
    elif n >= 2000:
        return slice( 10, 2000 )
    else:
        return slice( 0, 2000 )


def small_or_large_slice(n):
    """
        Given an integer n, return a slice with "