
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[-1]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[-2]

def get_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[-1]

def get_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return min(lst, key=lst.count)[-1]

def get_value_from_list_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return mean(lst, key=lst.count)[-1]

def get_value_from_list_with_std(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return std(lst, key=lst.count)[-1]

def get_value_from_list_with_median(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return median(lst, key=lst.count)[-1]

def get_value_from_list_with_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return min(lst, key