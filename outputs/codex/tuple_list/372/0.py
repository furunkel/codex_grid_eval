
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[0]


def extract_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]


def count_match_index(lst):
    """
    Given a list of numbers, write a function to count how many numbers are less than the number at the current index.
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


def oldest_customer(lst):
    """
    Given a list of dictionaries, write a function to return the oldest customer.
    """
    return max(lst, key=lambda x: x['age'])


def youngest_customer(lst):
    """
    Given a list of dictionaries, write a function to return the youngest customer.
    """
    return min(lst, key=lambda x: x['age'])


def oldest_customer_name(lst):
    """
    Given a list of dictionaries, write a function to return the name of the oldest customer.
    """
    return max(lst, key=lambda x: x['age'])['name']


def youngest_customer_name(lst):
    """
    Given a list of dictionaries, write a function to return the name of the youngest customer.
    """
    return min(lst, key=lambda x: x['age'])['name']


def increase_prices(lst, num):
    """
    Given a list of dictionaries,