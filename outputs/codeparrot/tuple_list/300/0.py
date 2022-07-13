
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
#    print lst
    if len(lst) == 0:
        return None
    return max(lst)[1]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
    if len(lst) == 0:
        return None
    return max(lst)[0]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
    if len(lst) == 0:
        return None
    return max(lst)[1]

def get_value_from_list_with_index(lst, index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
    if len(lst) == 0:
        return None
    return max(lst)[index]

def get_value_from_list_with_value(lst, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
    if len(lst) == 0:
        return None
    return max(lst)[value]

def get_value_from_list_with_index_and_value(lst, index, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
    if len(lst) == 0:
        return None
    return max(lst)[index][value]

def get_value_from_list_with_value_and_index(lst, value, index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value and index.
    """
    if len(lst) == 0:
        return None
    return max(lst)[index][value]

def get_value_from_list_with_value_and_index_and_value(lst, value, index, value):
    """