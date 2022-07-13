
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
#    print(lst)
    if len(lst) == 0:
        return None
    return max(lst, key=lambda x: x[1])[0]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest third value.
    """
    return min(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return mean(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_std(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return std(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_median(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return median(lst, key=lambda x: