
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < 0:
        return "mouse"
    elif n <= -1:
        return None
    else:
        return "small"

def small_or_large_list(l):
    """
        Given a list of integers, return "mouse" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if l == []:
        return "mouse"
    elif l == [-100]:
        return None
    else:
        return "small"

def small_or_large_dict(d):
    """
        Given a dictionary, return "mouse" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if d == {}:
        return "mouse"
    elif d == {-100:None}:
        return None
    else:
        return "small"

def small_or_large_tuple(t):
    """
        Given a tuple, return "mouse" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if t == ():
        return "mouse"
    elif t == (-100,):
        return None
    else:
        return "small"

def small_or_large_set(s):
    """
        Given a set, return "mouse" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if s == set():
        return "mouse"
    elif s == {-100}:
        return None
    else:
        return "small"

def small_or_large_frozenset(s):
    """
        Given a frozenset, return "mouse" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if s == frozenset():
        return "mouse"
    elif s == frozenset({-100}):
        return None
    else:
        return "small"

def small_or_large_slice(s):
    """
        Given a slice, return "mouse" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if s == slice():
        return "mouse"
    elif s == slice(-100,None):
        return None
    else:
        return "small"

def small_or_large_slice(s):
    """
        Given a slice, return "mouse" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if s == slice():
        return "mouse"
    elif s == slice(-100,None):
        return None
    else:
        return "small"

def small_or_large_slice(s):
    """
        Given a slice, return "mouse" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if s == slice():
        return "mouse"
    elif s == slice(-100,None):
        return None
    else:
        return "small"

def small_or_large_