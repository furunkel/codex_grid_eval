
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= 15 (and None if -100 <= n < 15).
    """
    if n < 0:
        return "mouse"
    elif n >= 15:
        return "large"
    else:
        return None


def small_or_large_reverse(n):
    """
        Given an integer n, return "large" if n < -15 and "mouse" if n >= -15 (and None if -15 <= n < -15).
    """
    if n < 0:
        return "large"
    elif n >= -15:
        return "mouse"
    else:
        return None


def small_or_large_and_large(n):
    """
        Given an integer n, return "mouse" if n < -15 and "large" if n >= -15 and "large" if n >= 15 (and None if -15 <= n < -15 or 15 <= n < -15).
    """
    if n < 0:
        return "mouse"
    elif n >= -15:
        return "large"
    elif n >= 15:
        return "large"
    else:
        return None


def small_or_large_and_large_reverse(n):
    """
        Given an integer n, return "large" if n < -15 and "mouse" if n >= -15 and "large" if n >= -15 and "mouse" if n >= 15 (and None if -15 <= n < -15 or 15 <= n < -15 or -15 <= n < 15).
    """
    if n < 0:
        return "mouse"
    elif n >= -15:
        return "large"
    elif n >= 15:
        return "large"
    elif n >= -15:
        return "mouse"
    else:
        return None


def small_or_large_and_large_and_large(n):
    """
        Given an integer n, return "mouse" if n < -15 and "large" if n >= -15 and "large" if n >= -15 and "large" if n >= 15 and "mouse" if n >= -15 and "large" if n >= -15 and "mouse" if n >= 15 (and None if -15 <= n < -15 or 15 <= n < -15 or -15 <= n < 15 or 15 <= n < -15 or -15 <= n < 15).
    """
    if n < 0:
        return "mouse"
    elif n >= -15:
        return "large"
    elif n >= 15:
        return "large"
    elif n >= -15:
        return "large"
    elif n >= 15:
        return "mouse"
    elif n >= -15:
        return "mouse"
    elif n >= 15:
        return "mouse"
    else:
        return None


def small_or_large_and_large_and_large_reverse(n):
    """
        Given an integer n, return "large" if n < -15 and "mouse" if n >= -15 and "large" if n >= -15 and "large" if n >= -15 and "mouse" if n >= -15 and "large" if n >= -15 and "mouse" if n >= -15 and "large" if n >= -15 and "mouse" if n 