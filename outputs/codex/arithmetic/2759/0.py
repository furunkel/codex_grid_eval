
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The third element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
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
    The key "first" contains the value of a.
    The key "second" contains the value of b.
    The key "third" contains the value of c.
    """
    return {"first": a, "second": b, "third": c}


def make_set(a, b, c):
    """
    Given three integers a, b and c, return a set where:
    The set contains the sum of the three numbers.
    The set contains the product of the three numbers.
    The set contains the largest of the three numbers.
    The set contains the smallest of the three numbers.
    """
    return {a + b + c, a * b * c, max(a, b, c), min(a, b, c)}


def make_list_of_dicts(a, b, c):
    """
    Given three integers a, b and c, return a list of dictionaries where:
    The first dictionary contains the key "first" and the value a.
    The second dictionary contains the key "second" and the value b.
    The third dictionary contains the key "third" and the value c.
    """
    return [{"first": a}, {"second": b}, {"third": c}]


def make_list_of_tuples(a, b, c):
    """
    Given three integers a, b and c, return a list of tuples where:
    The first tuple contains the sum of the three numbers.
    The second tuple contains