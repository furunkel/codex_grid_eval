
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
#    print(lst)
    return min(lst)[0]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
    return min(lst)[1]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
    return min(lst)[0]

def get_value_from_list_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
    return min(lst)[1]

def get_value_from_list_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    return max(lst)[0]

def get_value_from_list_with_min_value_and_max_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value and the largest twelfth value.
    """
    return min(lst)[1], max(lst)[1]

def get_value_from_list_with_max_value_and_min_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value and the largest twelfth value.
    """
    return max(lst)[0], min(lst)[1]

def get_value_from_list_with_min_value_and_max_value_and_min_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value and the largest twelfth value.
    """
    return min(lst)[0], max(lst)[0], min(