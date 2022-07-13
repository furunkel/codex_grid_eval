
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return (b - a, b * a, b + a)


def make_list(a, b, c):
    """
    Given three integers a, b and c, return a list where:
    The first element contains the product of the three numbers.
    The second element contains the sum of the three numbers.
    The third element contains the average of the three numbers.
    The fourth element contains the smallest number.
    The fifth element contains the largest number.
    """
    return [a * b * c, a + b + c, (a + b + c) / 3, min(a, b, c), max(a, b, c)]


def make_string(a, b, c):
    """
    Given three integers a, b and c, return a string where:
    The first two characters contain the ascii character representation of the first integer (i.e. '97' would refer to 'a').
    The second two characters contain the ascii character representation of the second integer (i.e. '98' would refer to 'b').
    The final two characters contain the ascii character representation of the third integer (i.e. '99' would refer to 'c').
    """
    return chr(a) + chr(b) + chr(c)


def make_dictionary(a, b, c):
    """
    Given three integers a, b and c, return a dictionary where:
    The key 'a' contains the first integer.
    The key 'b' contains the second integer.
    The key 'c' contains the third integer.
    """
    return {'a': a, 'b': b, 'c': c}


def make_set(a, b, c):
    """
    Given three integers a, b and c, return a set where:
    The set contains the product of the three numbers.
    The set contains the sum of the three numbers.
    The set contains the smallest number.
    The set contains the largest number.
    """
    return {a * b * c, a + b + c, min(a, b, c), max(a, b, c)}


def make_frozenset(a,