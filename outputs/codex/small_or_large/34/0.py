
def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 15 (and "neither" if -100 <= n < 15).
    """
    if n < -100:
        return "small"
    elif n >= 15:
        return "large"
    else:
        return "neither"


def small_or_large_v2(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 15 (and "neither" if -100 <= n < 15).
    """
    if n < -100:
        return "small"
    if n >= 15:
        return "large"
    return "neither"


def small_or_large_v3(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 15 (and "neither" if -100 <= n < 15).
    """
    if n < -100:
        return "small"
    return "large" if n >= 15 else "neither"


def small_or_large_v4(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 15 (and "neither" if -100 <= n < 15).
    """
    return "small" if n < -100 else "large" if n >= 15 else "neither"


def small_or_large_v5(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 15 (and "neither" if -100 <= n < 15).
    """
    return "small" if n < -100 else "large" if n >= 15 else "neither"


def small_or_large_v6(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 15 (and "neither" if -100 <= n < 15).
    """
    return "small" if n < -100 else "large" if n >= 15 else "neither"


def small_or_large_v7(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 15 (and "neither" if