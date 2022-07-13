
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
#    print lst
    return max(lst, key=lst.count)[0]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return max(lst, key=lst.count)[1]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return max(lst, key=lst.count)[0]

def get_value_from_list_with_index(lst, index):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return max(lst, key=lst.count)[index]

def get_value_from_list_with_index_and_value(lst, index, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return max(lst, key=lst.count)[index][value]

def get_value_from_list_with_index_and_value_and_index(lst, index, value, index_and_value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value and index.
    """
    return max(lst, key=lst.count)[index][value][index_and_value]

def get_value_from_list_with_index_and_value_and_index_and_value(lst, index, value, index_and_value, index_and_value_and_index):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value and index and index and value.
    """
    return max(lst, key=lst.count)[index][value][index_and_value][index_and_value_and_index]

def get_value_from_list_with_index_and_value_