
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "house" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if n < -100:
        return "mouse"
    elif n >= 2000:
        return "house"
    else:
        return None


def small_or_large_list(l):
    """
        Given a list of integers, return "mouse" if n < -100 and "house" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if l == []:
        return None
    elif l[0] < -100:
        return "mouse"
    elif l[0] >= 2000:
        return "house"
    else:
        return None


def small_or_large_dict(d):
    """
        Given a dictionary, return "mouse" if n < -100 and "house" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if d == {}:
        return None
    elif d["key"] < -100:
        return "mouse"
    elif d["key"] >= 2000:
        return "house"
    else:
        return None


def small_or_large_set(s):
    """
        Given a set, return "mouse" if n < -100 and "house" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if s == set():
        return None
    elif s[0] < -100:
        return "mouse"
    elif s[0] >= 2000:
        return "house"
    else:
        return None


def small_or_large_ordered_dict(d):
    """
        Given an ordered dictionary, return "mouse" if n < -100 and "house" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if d == OrderedDict():
        return None
    elif d["key"] < -100:
        return "mouse"
    elif d["key"] >= 2000:
        return "house"
    else:
        return None


def small_or_large_ordered_set(s):
    """
        Given an ordered set, return "mouse" if n < -100 and "house" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if s == OrderedSet():
        return None
    elif s[0] < -100:
        return "mouse"
    elif s[0] >= 2000:
        return "house"
    else:
        return None


def small_or_large_ordered_list(l):
    """
        Given an ordered list, return "mouse" if n < -100 and "house" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if l == []:
        return None
    elif l[0] < -100:
        return "mouse"
    elif l[0] >= 2000:
        return "house"
    else:
        return None


def small_or_large_ordered_dict(d):
    """
        Given an ordered dictionary, return "mouse" if n < -100 and "house" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if d == OrderedDict():
        return None
    elif d["key"] < -100:
        return "mouse"
    elif d["