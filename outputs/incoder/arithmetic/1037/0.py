
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return (a-b, b+a, a*b)

def make_tuple_of_tuples(*args):
    """
    Given any number of tuples, return a tuple of tuples.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_lists(*args):
    """
    Given any number of lists, return a tuple of lists.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_sets(*args):
    """
    Given any number of sets, return a tuple of sets.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_dicts(*args):
    """
    Given any number of dicts, return a tuple of dicts.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_tuples_of_tuples(*args):
    """
    Given any number of tuples of tuples, return a tuple of tuples of tuples.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_tuples_of_lists(*args):
    """
    Given any number of tuples of lists, return a tuple of tuples of lists.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_tuples_of_sets(*args):
    """
    Given any number of tuples of sets, return a tuple of tuples of sets.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_tuples_of_dicts(*args):
    """
    Given any number of tuples of dicts, return a tuple of tuples of dicts.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_tuples_of_tuples_of_tuples(*args):
    """
    Given any number of tuples of tuples of tuples, return a tuple of tuples of tuples of tuples.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_tuples_of_tuples_of_lists(*args):
    """
    Given any number of tuples of tuples of lists, return a tuple of tuples of tuples of lists.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_tuples_of_tuples_of_sets(*args):
    """
    Given any number of tuples of tuples of sets, return a tuple of tuples of tuples of sets.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_tuples_of_tuples_of_dicts(*args):
    """
    Given any number of tuples of tuples of dicts, return a tuple of tuples of tuples of dicts.
    """
    return tuple([make_tuple(*args) for args in args])

def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(*args):