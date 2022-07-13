
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "large"
    elif n >= 2:
        return "house"
    else:
        return None


@register.filter
def small_or_large_p(n, small):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "large"
    elif n >= 2:
        return "house"
    else:
        return small


@register.filter
def small_or_large_s(n, small):
    """
        Given an integer n, return "small" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "small"
    elif n >= 2:
        return "house"
    else:
        return small


@register.filter
def small_or_large_l(n, small):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "large"
    elif n >= 2:
        return "house"
    else:
        return small


@register.filter
def small_or_large_xl(n, small):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "large"
    elif n >= 2:
        return "house"
    else:
        return small


@register.filter
def small_or_large_xxl(n, small):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "large"
    elif n >= 2:
        return "house"
    else:
        return small


@register.filter
def small_or_large_xxxl(n, small):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "large"
    elif n >= 2:
        return "house"
    else:
        return small


@register.filter
def small_or_large_xxxxl(n, small):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "large"
    elif n >= 2:
        return "house"
    else:
        return small


@register.filter
def small_or_large_xxxxl(n, small):
    """
        Given an integer n, return "large" if n < -100 and "house" if n 