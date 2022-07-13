
def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < 0:
        return "small"
    elif n >= -1:
        return "large"
    else:
        return None


def small_or_large_list(l):
    """
        Given a list of integers, return "small" if all elements are < -100 and "large" if all elements are >= -1 (and None if -100 <= n < -1).
    """
    small_or_large_list = []
    for n in l:
        small_or_large_list.append(small_or_large(n))
    return small_or_large_list


def small_or_large_dict(d):
    """
        Given a dictionary, return "small" if all values are < -100 and "large" if all values are >= -1 (and None if -100 <= n < -1).
    """
    small_or_large_dict = {}
    for k in d:
        small_or_large_dict[k] = small_or_large(d[k])
    return small_or_large_dict


def small_or_large_set(s):
    """
        Given a set, return "small" if all elements are < -100 and "large" if all elements are >= -1 (and None if -100 <= n < -1).
    """
    small_or_large_set = set()
    for n in s:
        small_or_large_set.add(small_or_large(n))
    return small_or_large_set


def small_or_large_dict(d):
    """
        Given a dictionary, return "small" if all values are < -100 and "large" if all values are >= -1 (and None if -100 <= n < -1).
    """
    small_or_large_dict = {}
    for k in d:
        small_or_large_dict[k] = small_or_large(d[k])
    return small_or_large_dict


def small_or_large_set(s):
    """
        Given a set, return "small" if all elements are < -100 and "large" if all elements are >= -1 (and None if -100 <= n < -1).
    """
    small_or_large_set = set()
    for n in s:
        small_or_large_set.add(small_or_large(n))
    return small_or_large_set


def small_or_large_dict(d):
    """
        Given a dictionary, return "small" if all values are < -100 and "large" if all values are >= -1 (and None if -100 <= n < -1).
    """
    small_or_large_dict = {}
    for k in d:
        small_or_large_dict[k] = small_or_large(d[k])
    return small_or_large_dict


def small_or_large_set(s):
    """
        Given a set, return "small" if all elements are < -100 and "large" if all elements are >= -1 (and None if -100 <= n < -1).
    """
    small_or_large_set = set()
    for n in s:
        small_or_large_set.add(small_or_large(n))
    return small_or_large_set


def small_or_large_