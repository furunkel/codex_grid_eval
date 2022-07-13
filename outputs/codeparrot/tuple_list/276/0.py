
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
#    print(lst)
    if len(lst) == 0:
        return 0
    return max(lst, key=lambda x: x[1])[1]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_min_max_and_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value and the minimum value.
    """
    return max(lst, key=lambda x: x[1])[1], min(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_min_max_and_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value and the minimum value and the maximum value.
    """
    return max(lst, key=lambda x: x[1], min(lst, key=lambda x: x[1])[1], max(lst, key=lambda x: x[1])[1], min(lst, key=lambda x: x[1])[1])

def get_value_from_list_with_min_max_and_min_and_max_and_min(lst):
    """
    Given a