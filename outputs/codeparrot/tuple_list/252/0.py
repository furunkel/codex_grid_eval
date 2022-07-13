
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
#    print(lst)
    if len(lst) == 0:
        return 0
    return max(lst)[0]

def get_twelfth_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
    if len(lst) == 0:
        return 0
    return max(lst)[1]

def get_twelfth_value_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
    if len(lst) == 0:
        return 0
    return min(lst)[0]

def get_twelfth_value_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    if len(lst) == 0:
        return 0
    return max(lst)[1]

def get_twelfth_value_with_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
    if len(lst) == 0:
        return 0
    return min(lst)[0], max(lst)[1]

def get_twelfth_value_with_max_and_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    if len(lst) == 0:
        return 0
    return max(lst)[0], min(lst)[1]

def get_twelfth_value_with_min_and_max_and_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
    if len