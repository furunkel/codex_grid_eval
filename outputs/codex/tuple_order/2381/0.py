
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The first element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    """
    return (b + a, b * a, b - a)


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
    key "val_1" has the value of the sum of the three numbers.
    key "val_2" has the value of the product of the three numbers.
    key "val_3" has the value of the smallest number.
    key "val_4" has the value of the largest number.
    """
    return {"val_1": a + b + c, "val_2": a * b * c, "val_3": min(a, b, c), "val_4": max(a, b, c)}


def make_set(a, b, c):
    """
    Given three integers a, b and c, return a set with:
    The product of the three numbers.
    The sum of the three numbers.
    """
    return {a * b * c, a + b + c}


def make_tuple_of_lists(a, b, c):
    """
    Given three integers a, b and c, return a tuple where:
    The first element is a list with the sum of the three numbers.
    The second element is a set with the product of the three numbers.
    """
    return ([a + b + c], {a * b * c})


def make_list_of_tuples(a, b, c):
    """
    Given three integers a, b and c, return a list where:
    The first element is a tuple with the sum of the three numbers.
    The second element is a tuple with the product of the three numbers.