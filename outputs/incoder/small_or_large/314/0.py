
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 15 (and None if 10 <= n < 15).
    """
    if n < 10:
        return "mouse"
    elif n >= 15:
        return "large"
    else:
        return None


def small_or_large_list(l):
    """
        Given a list of integers, return "mouse" if n < 10 and "large" if n >= 15 (and None if 10 <= n < 15).
    """
    if l == []:
        return "mouse"
    elif l == [None]:
        return "mouse"
    elif l[0] < 10:
        return "mouse"
    elif l[0] >= 15:
        return "large"
    else:
        return None


def small_or_large_dict(d):
    """
        Given a dictionary, return "mouse" if n < 10 and "large" if n >= 15 (and None if 10 <= n < 15).
    """
    if d == {}:
        return "mouse"
    elif d == {None}:
        return "mouse"
    elif d[0] < 10:
        return "mouse"
    elif d[0] >= 15:
        return "large"
    else:
        return None


def small_or_large_set(s):
    """
        Given a set, return "mouse" if n < 10 and "large" if n >= 15 (and None if 10 <= n < 15).
    """
    if s == set():
        return "mouse"
    elif s == {None}:
        return "mouse"
    elif s[0] < 10:
        return "mouse"
    elif s[0] >= 15:
        return "large"
    else:
        return None


def small_or_large_tuple(t):
    """
        Given a tuple, return "mouse" if n < 10 and "large" if n >= 15 (and None if 10 <= n < 15).
    """
    if t == tuple():
        return "mouse"
    elif t == (None,):
        return "mouse"
    elif t[0] < 10:
        return "mouse"
    elif t[0] >= 15:
        return "large"
    else:
        return None


def small_or_large_frozenset(s):
    """
        Given a frozenset, return "mouse" if n < 10 and "large" if n >= 15 (and None if 10 <= n < 15).
    """
    if s == frozenset():
        return "mouse"
    elif s == frozenset({None}):
        return "mouse"
    elif s[0] < 10:
        return "mouse"
    elif s[0] >= 15:
        return "large"
    else:
        return None


def small_or_large_slice(s):
    """
        Given a slice, return "mouse" if n < 10 and "large" if n >= 15 (and None if 10 <= n < 15).
    """
    if s == slice():
        return "mouse"
    elif s == slice(None):
        return "mouse"
    elif s.start < 10:
        return "mouse"
    elif s.start >= 15:
        return "large"
    else:
        return None


def small_or_large_slice(s):
    """
        Given a slice