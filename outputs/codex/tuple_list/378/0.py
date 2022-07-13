
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lambda x: x[1])[0]


def extract_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]


def count_match_index(lst):
    """
    Given a list of numbers, write a function to count how many numbers are less than the number at the index.
    """
    return sum(1 for i, x in enumerate(lst) if x < lst[i])


def remove_negatives(lst):
    """
    Given a list of numbers, write a function to remove any negative numbers.
    """
    return [x for x in lst if x >= 0]


def order_by_age(lst):
    """
    Given a list of dictionaries, write a function to return a list of dictionaries ordered by age.
    """
    return sorted(lst, key=lambda x: x['age'])


def oldest_student(lst):
    """
    Given a list of dictionaries, write a function to return the name of the oldest student.
    """
    return max(lst, key=lambda x: x['age'])['name']


def youngest_student(lst):
    """
    Given a list of dictionaries, write a function to return the name of the youngest student.
    """
    return min(lst, key=lambda x: x['age'])['name']


def find_student(lst, name):
    """
    Given a list of dictionaries and a name, write a function to return the age of the student with that name.
    """
    return next(x['age'] for x in lst if x['name'] == name)


def find_in_nested_list(lst, value):
    """
    Given a list of lists and a value, write a function to return the index of the inner list that contains that value.
    """
    return next(i for i, x in enumerate(lst) if value in x)