
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    return (b * a, b - a, b + a)


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
    The set contains the three integers.
    """
    return {a, b, c}


def make_tuple_from_list(lst):
    """
    Given a list of integers, return a tuple where:
    The second element contains the sum of the elements in the list.
    The first element contains the product of the elements in the list.
    """
    return (reduce(lambda x, y: x * y, lst), reduce(lambda x, y: x + y, lst))


def make_list_from_tuple(tup):
    """
    Given a tuple of integers, return a list where:
    The first element contains the sum of the elements in the tuple.
    The second element contains the product of the elements in the tuple.
    """
    return [reduce(lambda x, y: x + y, tup), reduce(lambda x, y: x * y, tup)]


def make_dict_from_list(lst):
    """
    Given a list of integers, return a dictionary where:
    The keys are the