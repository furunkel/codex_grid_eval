
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
#    print(lst)
    return max(lst, key=lst.count)[1]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return max(lst, key=lst.count)[0]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return max(lst, key=lst.count)[1]

def get_value_from_list_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return max(lst, key=lst.count)[0]

def get_value_from_list_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return max(lst, key=lst.count)[1]

def get_value_from_list_with_min_value_and_max_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value and the maximum second value.
    """
    return max(lst, key=lst.count)[0], max(lst, key=lst.count)[1]

def get_value_from_list_with_max_value_and_min_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value and the minimum second value.
    """
    return max(lst, key=lst.count)[0], min(lst, key=lst.count)[1]

def get_value_from_list_with_min_value_and_max_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value and the minimum second value.
    """
   