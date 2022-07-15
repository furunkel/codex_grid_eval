
def make_tuple(fkrjf4ifji4ofj, a):
    """
    Given two integers fkrjf4ifji4ofj and a, return a tuple where:
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return (fkrjf4ifji4ofj - a, fkrjf4ifji4ofj * a, fkrjf4ifji4ofj + a)

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
    Given three integers a, b and c, return a set that contains:
    The product of a and b.
    The sum of a and b.
    The sum of b and c.
    The product of b and c.
    The product of a and c.
    """
    return {a * b, a + b, b + c, b * c, a * c}

def make_string(a, b, c):
    """
    Given three integers a, b and c, return a string that contains:
    The product of a and b on one line.
    The sum of a and b on the next line.
    The sum of b and c on the next line.
    The product of b and c on the next line.
    The product of a and c on the next line.
    """
    return '{}\n{}\n{}\n{}\n{}'.format(a * b, a + b, b + c, b * c, a * c)

def make_list_of_dicts