
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return (b * a, b + a, b - a)


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


def make_string(a, b, c):
    """
    Given three integers a, b and c, return a string where:
    The string contains the three integers concatenated, in that order, separated by commas.
    """
    return str(a) + ',' + str(b) + ',' + str(c)


def make_list_of_strings(a, b, c):
    """
    Given three integers a, b and c, return a list of strings where:
    The first string contains the integer a as a string.
    The second string contains the integer b as a string.
    The third string contains the integer c as a string.
    """
    return [str(a), str(b), str(c)]


def make_list_of_numbers(a, b, c):
    """
    Given three integers a, b and c, return a list of numbers where:
    The first element contains the integer a.