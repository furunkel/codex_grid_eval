
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    """
    return (b - a, b + a, b * a)


def make_list(a, b, c):
    """
    Given three integers a, b and c, return a list where:
    The first element contains the sum of the three numbers.
    The second element contains the product of the three numbers.
    """
    return [a + b + c, a * b * c]


def make_dict(a, b, c):
    """
    Given three integers a, b and c, return a dictionary where:
    key "val_1" with value a
    key "val_2" with value b
    key "val_3" with value c
    """
    return {"val_1": a, "val_2": b, "val_3": c}


def make_set(a, b, c):
    """
    Given three integers a, b and c, return a set with:
    Integer a
    Integer b
    Integer c
    """
    return {a, b, c}


def make_string(a, b, c):
    """
    Given three integers a, b and c, return a string with:
    The product of the three numbers.
    """
    return str(a * b * c)


def make_list_of_strings(a, b, c):
    """
    Given three integers a, b and c, return a list of strings with:
    The product of the three numbers.
    """
    return [str(a * b * c)]


def make_list_of_tuples(a, b, c):
    """
    Given three integers a, b and c, return a list of tuples where:
    The first element contains the sum of the three numbers.
    The second element contains the product of the three numbers.
    """
    return [(a + b + c, a * b * c)]


def make_dict_of_lists(a, b, c):
    """
    Given three integers a, b and c, return a dictionary of lists where:
    key "val_1" with value [a, b, c]
    key "val_2" with value [b,