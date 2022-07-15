
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return (a - b, a * b, a + b)


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
    The first two characters contain the ascii character representation of the first integer (i.e. the character with the ascii code of a).
    The second two characters contain the ascii character representation of the second integer (i.e. the character with the ascii code of b).
    The third two characters contain the ascii character representation of the third integer (i.e. the character with the ascii code of c).
    The fourth two characters contain the ascii character representation of the fourth integer (i.e. the character with the ascii code of a + 1).
    The fifth two characters contain the ascii character representation of the fifth integer (i.e. the character with the ascii code of b + 1).
    The sixth two characters contain the ascii character representation of the sixth integer (i.e. the character with the ascii code of c + 1).
    """
    return chr(a) + chr(b) + chr(c) + chr(a + 1) + chr(b + 1) + chr(c + 1)


def make_dict(a, b, c):
    """
    Given three integers a, b and c, return a dictionary where:
    The key 'a' contains the first integer.
    The key 'b' contains the second integer.
    The key 'c' contains the third integer.
    """
    return {'a