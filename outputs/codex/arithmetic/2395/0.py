
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return (b * a, b - a, b + a)


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
    The first element contains the product of the three numbers.
    The second element contains the sum of the three numbers.
    The third element contains the average of the three numbers.
    The fourth element contains the smallest number.
    The fifth element contains the largest number.
    """
    return "The product is {}. The sum is {}. The average is {}. The minimum is {}. The maximum is {}.".format(
        a * b * c, a + b + c, (a + b + c) / 3, min(a, b, c), max(a, b, c))


def make_dict(a, b, c):
    """
    Given three integers a, b and c, return a dictionary where:
    The first element contains the product of the three numbers.
    The second element contains the sum of the three numbers.
    The third element contains the average of the three numbers.
    The fourth element contains the smallest number.
    The fifth element contains the largest number.
    """
    return {
        "product": a * b * c,
        "sum": a + b + c,
        "average": (a + b + c) / 3,
        "minimum": min(a, b, c),
        "maximum": max(a, b, c)
    }


def make_set(a, b, c):
    """
    Given three integers a, b and c, return a set