
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    elif n >= 2000:
        return "large"
    else:
        return None

def small_or_large_v2(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    if n >= 2000:
        return "large"
    return None

def small_or_large_v3(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    if n >= 2000:
        return "large"
    if 10 <= n < 2000:
        return None

def small_or_large_v4(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    if n >= 2000:
        return "large"
    if n >= 10:
        if n < 2000:
            return None

def small_or_large_v5(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    if n >= 2000:
        return "large"
    if n >= 10:
        if n < 2000:
            return None
        else:
            return "large"

def small_or_large_v6(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    if n >= 2000:
        return "large"
    if n >= 10:
        if n < 2000:
            return None
