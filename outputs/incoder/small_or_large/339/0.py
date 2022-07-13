
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if n < -100:
        return "mouse"
    elif n >= 2000:
        return "small"
    else:
        return None


def small_or_large_list(l):
    """
        Given a list of integers, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if l == []:
        return "mouse"
    elif len(l) >= 2:
        return "small"
    else:
        return None


def small_or_large_dict(d):
    """
        Given a dictionary, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if d == {}:
        return "mouse"
    elif len(d) >= 2:
        return "small"
    else:
        return None


def small_or_large_set(s):
    """
        Given a set, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if s == set():
        return "mouse"
    elif len(s) >= 2:
        return "small"
    else:
        return None


def small_or_large_str(s):
    """
        Given a string, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if s == "":
        return "mouse"
    elif len(s) >= 2:
        return "small"
    else:
        return None


def small_or_large_bool(s):
    """
        Given a boolean, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if s == True:
        return "mouse"
    elif s == False:
        return "small"
    else:
        return None


def small_or_large_float(s):
    """
        Given a float, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if s == 0.0:
        return "mouse"
    elif s == 1.0:
        return "small"
    else:
        return None


def small_or_large_complex(s):
    """
        Given a complex, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if s == complex(0, 0):
        return "mouse"
    elif s == complex(1, 0):
        return "small"
    else:
        return None


def small_or_large_date(s):
    """
        Given a date, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if s == datetime.date.today():
        return "mouse"
    elif s == datetime.date.today() + datetime.timedelta(days=1):
        return "small"
    else:
        return None


def small_or_large_