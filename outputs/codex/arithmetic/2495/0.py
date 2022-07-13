
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return (b + a, b - a, b * a)


def make_list(a, b, c):
    """
    Given three integers a, b and c, return a list where:
    The first element contains the sum of the three numbers.
    The second element contains the product of the three numbers.
    The third element contains the largest of the three numbers.
    The fourth element contains the smallest of the three numbers.
    """
    return [a + b + c, a * b * c, max(a, b, c), min(a, b, c)]


def make_dict(a, b, c):
    """
    Given three integers a, b and c, return a dictionary where:
    The key 'a' contains the value of a.
    The key 'b' contains the value of b.
    The key 'c' contains the value of c.
    """
    return {'a': a, 'b': b, 'c': c}


def make_set(a, b, c):
    """
    Given three integers a, b and c, return a set where:
    The set contains the integers a, b and c.
    """
    return {a, b, c}


def make_frozenset(a, b, c):
    """
    Given three integers a, b and c, return a frozenset where:
    The frozenset contains the integers a, b and c.
    """
    return frozenset([a, b, c])


def make_list_of_tuples(a, b, c):
    """
    Given three integers a, b and c, return a list of tuples where:
    The first tuple contains the integers a, b and c.
    The second tuple contains the integers a, b and c.
    The third tuple contains the integers a, b and c.
    """
    return [(a, b, c), (a, b, c), (a, b, c)]


def make_list_of_lists(a, b, c):
    """
    Given three integers a, b and c, return a list of lists where:
    The first list contains the integers a, b