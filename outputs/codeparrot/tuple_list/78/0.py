
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
#    print lst
    if len(lst) == 0:
        return None
    return max(lst, key=lst.count)[0]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
#    print lst
    if len(lst) == 0:
        return None
    return max(lst, key=lst.count)[0]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
#    print lst
    if len(lst) == 0:
        return None
    return max(lst, key=lst.count)[0]

def get_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
#    print lst
    if len(lst) == 0:
        return None
    return max(lst, key=lst.count)[0]

def get_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
#    print lst
    if len(lst) == 0:
        return None
    return min(lst, key=lst.count)[0]

def get_value_from_list_with_avg(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
#    print lst
    if len(lst) == 0:
        return None
    return avg(lst, key=lst.count)[0]

def get_value_from_list_with_std(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
#    print lst
    if len(lst) == 0:
        return None
    return std(lst, key=lst.count)[0]
