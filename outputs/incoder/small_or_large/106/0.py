
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 10 and "house" if n >= 15 (and None if 10 <= n < 15).
    """
    if n < 10:
        return "small"
    elif n >= 15:
        return "large"
    else:
        return None


def small_or_large_list(l):
    """
        Given a list of integers, return "small" if any element < 10 and "house" if any element >= 15 (and None if 10 <= element < 15).
    """
    if any(n < 10 for n in l):
        return "small"
    elif any(n >= 15 for n in l):
        return "large"
    else:
        return None


def small_or_large_dict(d):
    """
        Given a dictionary, return "small" if any element < 10 and "house" if any element >= 15 (and None if 10 <= element < 15).
    """
    if any(n < 10 for n in d.values()):
        return "small"
    elif any(n >= 15 for n in d.values()):
        return "large"
    else:
        return None


def small_or_large_dict_list(d):
    """
        Given a dictionary, return "small" if any element < 10 and "house" if any element >= 15 (and None if 10 <= element < 15).
    """
    if any(n < 10 for n in d.values()):
        return "small"
    elif any(n >= 15 for n in d.values()):
        return "large"
    else:
        return None


def small_or_large_dict_list_dict(d):
    """
        Given a dictionary, return "small" if any element < 10 and "house" if any element >= 15 (and None if 10 <= element < 15).
    """
    if any(n < 10 for n in d.values()):
        return "small"
    elif any(n >= 15 for n in d.values()):
        return "large"
    else:
        return None


def small_or_large_dict_list_dict_list(d):
    """
        Given a dictionary, return "small" if any element < 10 and "house" if any element >= 15 (and None if 10 <= element < 15).
    """
    if any(n < 10 for n in d.values()):
        return "small"
    elif any(n >= 15 for n in d.values()):
        return "large"
    else:
        return None


def small_or_large_dict_list_dict_list_dict(d):
    """
        Given a dictionary, return "small" if any element < 10 and "house" if any element >= 15 (and None if 10 <= element < 15).
    """
    if any(n < 10 for n in d.values()):
        return "small"
    elif any(n >= 15 for n in d.values()):
        return "large"
    else:
        return None


def small_or_large_dict_list_dict_list_dict_list(d):
    """
        Given a dictionary, return "small" if any element < 10 and "house" if any element >= 15 (and None if 10 <= element < 15).
