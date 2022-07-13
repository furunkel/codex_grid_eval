
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
#    print lst
    if len(lst) == 0:
        return 0
    return max(lst, key=lambda x: x[1])[0]

def get_twelfth_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    if len(lst) == 0:
        return 0
    return max(lst, key=lambda x: x[1])[1]

def get_twelfth_value_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    if len(lst) == 0:
        return 0
    return max(lst, key=lambda x: x[1])[1]

def get_twelfth_value_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
    if len(lst) == 0:
        return 0
    return min(lst, key=lambda x: x[1])[1]

def get_twelfth_value_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    if len(lst) == 0:
        return 0
    return mean(lst, key=lambda x: x[1])[1]

def get_twelfth_value_with_median(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    if len(lst) == 0:
        return 0
    return median(lst, key=lambda x: x[1])[1]

def get_twelfth_value_with_std(lst):
    """
    Given a list of tuples, write a function that returns the twe