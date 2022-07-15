
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    """
    return (b * a, b + a, b - a)


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


def make_tuple_from_list(l):
    """
    Given a list of integers, return a tuple where:
    The second element contains the sum of the elements.
    The first element contains the product of the elements.
    """
    return (reduce(lambda x, y: x * y, l), reduce(lambda x, y: x + y, l))


def make_list_from_tuple(t):
    """
    Given a tuple of integers, return a list where:
    The first element contains the sum of the elements.
    The second element contains the product of the elements.
    """
    return [reduce(lambda x, y: x + y, t), reduce(lambda x, y: x * y, t)]


def make_dict_from_list(l):
    """
    Given a list of integers, return a dictionary where:
    The key 'evens' has a list of the even elements of l.
    The key 'odds