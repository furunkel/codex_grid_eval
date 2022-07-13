
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    """
    return (a * b, a + b, a - b)


def make_list(a, b, c):
    """
    Given three integers a, b and c, return a list where:
    The first element contains the sum of the three numbers.
    The second element contains the product of the three numbers.
    The third element contains the smallest number.
    The fourth element contains the largest number.
    """
    return [a + b + c, a * b * c, min(a, b, c), max(a, b, c)]


def make_dict(a, b, c):
    """
    Given three integers a, b and c, return a dictionary where:
    The key 'a' has value equal to the first integer.
    The key 'b' has value equal to the second integer.
    The key 'c' has value equal to the third integer.
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
    The second element contains the sum of the list.
    The third element contains the product of the list.
    The first element contains the smallest number.
    The fourth element contains the largest number.
    """
    return (min(lst), sum(lst), reduce(lambda x, y: x * y, lst), max(lst))


def make_list_from_tuple(tpl):
    """
    Given a tuple of integers, return a list where:
    The first element contains the sum of the tuple.
    The second element contains the product of the tuple.
    The third element contains the smallest number.
    The fourth element contains the largest number.
    """
    return [sum(tpl), reduce(lambda x, y: x * y, tpl), min(tpl), max(tpl)]


def make_dict_from