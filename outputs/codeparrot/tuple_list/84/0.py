
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
#    print lst
    if len(lst) == 0:
        return None
    return max(lst)[1]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return max(lst)[0]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return max(lst)[1]

def get_value_from_list_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return max(lst)[0]

def get_value_from_list_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(lst)[1]

def get_value_from_list_with_min_value_and_max_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value and the largest second value.
    """
    return max(lst)[0], max(lst)[1]

def get_value_from_list_with_max_value_and_min_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value and the smallest second value.
    """
    return max(lst)[0], max(lst)[1]

def get_value_from_list_with_min_value_and_max_value_and_min_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value and the smallest second value.
    """
    return max(lst)[0], max(lst)[1], min(lst)[1]

def get_value_from_list_with_max_value_and_