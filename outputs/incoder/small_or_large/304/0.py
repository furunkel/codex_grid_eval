
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < 0:
        return "mouse"
    elif n > 0:
        return "large"
    else:
        return None


def small_or_large_recursive(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < 0:
        return "mouse"
    elif n > 0:
        return "large"
    else:
        return small_or_large_recursive(n - 1)


def small_or_large_iterative(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < 0:
        return "mouse"
    elif n > 0:
        return "large"
    else:
        small = small_or_large_iterative(n - 1)
        if small is None:
            return "mouse"
        else:
            return small


def small_or_large_iterative_recursive(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < 0:
        return "mouse"
    elif n > 0:
        return "large"
    else:
        small = small_or_large_iterative_recursive(n - 1)
        if small is None:
            return "mouse"
        else:
            return small


def small_or_large_iterative_iter(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < 0:
        return "mouse"
    elif n > 0:
        return "large"
    else:
        small = small_or_large_iterative_iter(n - 1)
        if small is None:
            return "mouse"
        else:
            return small


def small_or_large_iterative_iter_recursive(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < 0:
        return "mouse"
    elif n > 0:
        return "large"
    else:
        small = small_or_large_iterative_iter_recursive(n - 1)
        if small is None:
            return "mouse"
        else:
            return small


def small_or_large_iterative_iter_recursive_recursive(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < 0:
        return "mouse"
    elif n > 0:
        return "large"
    else:
        small = small_or_large_iterative_iter_recursive_recursive(n - 1)
        if small is None:
            return "mouse"
        else:
            return small


def small_or_large_iterative_