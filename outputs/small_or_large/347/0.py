
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    elif n >= 2000:
        return "small"
    else:
        return None

def small_or_large_2(n):
    """
        Given an integer n, return "mouse" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    if n >= 2000:
        return "small"
    return None

def small_or_large_3(n):
    """
        Given an integer n, return "mouse" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    if n >= 2000:
        return "small"
    if 10 <= n < 2000:
        return None

def small_or_large_4(n):
    """
        Given an integer n, return "mouse" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    if n >= 2000:
        return "small"
    if n >= 10 and n < 2000:
        return None

def small_or_large_5(n):
    """
        Given an integer n, return "mouse" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    if n >= 2000:
        return "small"
    if n >= 10:
        if n < 2000:
            return None

def small_or_large_6(n):
    """
        Given an integer n, return "mouse" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    if n >= 2000:
        return "small"
    if n >= 10:
        if n < 2000:
            return None
        else:
            return "small"

def small_or_large_