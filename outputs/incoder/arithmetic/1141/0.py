
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return (a+b, a*b, a-b)


def make_tuple_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return tuple(sum(list_of_tuples), prod(list_of_tuples), sum(list_of_tuples)-prod(list_of_tuples))


def make_tuple_of_lists(list_of_lists):
    """
    Given a list of lists, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return tuple(sum(list_of_lists), prod(list_of_lists), sum(list_of_lists)-prod(list_of_lists))


def make_tuple_of_sets(list_of_sets):
    """
    Given a list of sets, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return tuple(sum(list_of_sets), prod(list_of_sets), sum(list_of_sets)-prod(list_of_sets))


def make_tuple_of_dicts(list_of_dicts):
    """
    Given a list of dicts, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return tuple(sum(list_of_dicts), prod(list_of_dicts), sum(list_of_dicts)-prod(list_of_dicts))


def make_tuple_of_functions(list_of_functions):
    """
    Given a list of functions, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return tuple(sum(list_of_functions), prod(list_of_functions), sum(list_of_functions)-prod(list_of_functions))


def make_tuple_of_numbers(list_of_numbers):
    """
    Given a list of numbers, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return tuple(sum(list_of_numbers), prod(list_of_numbers), sum(list_of_numbers)-prod(list_of_numbers))


def make_tuple_of_strings(list_of_strings):
    """
    Given a list of strings, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (