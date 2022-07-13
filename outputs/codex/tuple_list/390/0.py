
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x: x[2])[-1]


def extract_full_name(lst):
    """
    Given a list of dictionaries, write a function that returns a new list of strings with the first and last name keys
    in each dictionary concatenated.
    """
    return [f"{d['first']} {d['last']}" for d in lst]


def create_class_ranking(lst):
    """
    Given a list of dictionaries, write a function that returns a dictionary with keys as the unique class names and
    values as the number of students in that class.
    """
    return {d['class']: lst.count(d) for d in lst}


def interleave(str1, str2):
    """
    Given two strings, write a function that returns the characters from the first string interleaved with the characters
    from the second string.
    """
    return "".join([x + y for x, y in zip(str1, str2)])


def triple_and_filter(lst):
    """
    Given a list of numbers, write a function that returns a list of those numbers multiplied by 3 and filtered to only
    show numbers greater than 10.
    """
    return [x * 3 for x in lst if x * 3 > 10]


def extract_full_name(lst):
    """
    Given a list of dictionaries, write a function that returns a list of strings with the first and last name keys in
    each dictionary concatenated.
    """
    return [f"{d['first']} {d['last']}" for d in lst]


def multiply_even_numbers(lst):
    """
    Given a list of numbers, write a function that returns the product of all the even numbers.
    """
    return reduce(lambda x, y: x * y, [x for x in lst if x % 2 == 0])


def capitalize(str):
    """
    Given a string, write a function that returns the same string with the first letter capitalized.
    """
    return str[0].upper() + str[1:]


def compact