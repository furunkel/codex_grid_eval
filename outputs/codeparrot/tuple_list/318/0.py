
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
#    print lst
    return max(lst, key=lst.count)

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[-1]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[-2]

def get_value_from_list_with_index(lst, index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[-index]

def get_value_from_list_with_value(lst, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[-value]

def get_value_from_list_with_index_and_value(lst, index, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[-index-1]

def get_value_from_list_with_value_and_index(lst, value, index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[-value-index-1]

def get_value_from_list_with_value_and_index_and_value(lst, value, index, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[-value-index-