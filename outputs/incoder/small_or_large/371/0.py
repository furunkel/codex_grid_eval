
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= 2000 (and neither if -100 <= n < 2000).
    """
    if n < -100:
        return "mouse"
    elif n >= 2000:
        return "small"
    else:
        return "large"

# --------------------------------------------------
# Functions for dealing with numbers
# --------------------------------------------------

def to_number(s):
    """
        Convert a number string to a number.
    """
    try:
        return int(s)
    except ValueError:
        return float(s)

def to_number_list(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return [to_number(s) for s in s.split(",")]

def to_number_tuple(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return tuple(to_number_list(s))

def to_number_set(s):
    """
        Convert a comma-separated string to a set of numbers.
    """
    return set(to_number_list(s))

def to_number_tuple(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return tuple(to_number_list(s))

def to_number_set(s):
    """
        Convert a comma-separated string to a set of numbers.
    """
    return set(to_number_list(s))

def to_number_list(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return [to_number(s) for s in s.split(",")]

def to_number_tuple(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return tuple(to_number_list(s))

def to_number_set(s):
    """
        Convert a comma-separated string to a set of numbers.
    """
    return set(to_number_list(s))

def to_number_list(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return [to_number(s) for s in s.split(",")]

def to_number_tuple(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return tuple(to_number_list(s))

def to_number_set(s):
    """
        Convert a comma-separated string to a set of numbers.
    """
    return set(to_number_list(s))

def to_number_list(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return [to_number(s) for s in s.split(",")]

def to_number_tuple(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return tuple(to_number_list(s))

def to_number_set(s):
    """
        Convert a comma-separated string to a set of numbers.
    """
    return set(to_number_list(s))

def to_number_list(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return [to_number(s) for s in s.split(",")]

def to_number_tuple(s):
    """
        Convert a comma-separated string to a list of numbers.
    """
    return tuple(to_number_list(s))

def to_number_set(s):
    """
        Convert a comma-separated string to a set of numbers.
    """