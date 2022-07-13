
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[-1]

def get_value_with_index(lst, index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[-index]

def get_value_with_index_and_value(lst, index, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value and the value.
    """
    return max(lst, key=lst.count)[-index-1] + value

def get_value_with_index_and_value_and_index(lst, index, value, index_and_value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value and the value.
    """
    return max(lst, key=lst.count)[-index-1] + value + index_and_value

def get_value_with_index_and_value_and_index_and_value(lst, index, value, index_and_value, index_and_value_and_index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value and the value.
    """
    return max(lst, key=lst.count)[-index-1] + value + index_and_value + index_and_value_and_index

def get_value_with_index_and_value_and_index_and_value_and_index(lst, index, value, index_and_value, index_and_value_and_index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple