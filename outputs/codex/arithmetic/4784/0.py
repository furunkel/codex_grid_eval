
def make_tuple(fkrjf4ifji4ofj, a):
    """
    Given two integers fkrjf4ifji4ofj and a, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    """
    return (fkrjf4ifji4ofj * a, fkrjf4ifji4ofj + a, fkrjf4ifji4ofj - a)

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
    The key 'first' contains the value of a.
    The key 'second' contains the value of b.
    The key 'third' contains the value of c.
    """
    return {'first': a, 'second': b, 'third': c}

def make_set(a, b, c):
    """
    Given three integers a, b and c, return a set where:
    The set contains the product of a and b.
    The set contains the sum of a and b.
    The set contains the sum of b and c.
    The set contains the product of b and c.
    The set contains the product of a and c.
    """
    return {a * b, a + b, b + c, b * c, a * c}

def make_string(a, b, c):
    """
    Given three integers a, b and c, return a string where:
    The string contains the product of a and b.
    The string contains the sum of a and b.
    The string contains the sum of b and c.
    The string contains the product of b and c.
    The string contains the product of a and c.
    """
    return str(a * b) + str(a + b) + str(b + c) + str(b * c) + str(a * c)

def make_list