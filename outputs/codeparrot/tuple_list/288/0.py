
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
#    print(lst)
    return max(lst, key=lst.count)[0]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
#    print(lst)
    return max(lst, key=lst.count)[0]

def get_value_with_index(lst, index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
#    print(lst)
    return max(lst, key=lst.count)[index]

def get_value_with_value(lst, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
#    print(lst)
    return max(lst, key=lst.count)[value]

def get_value_with_index_and_value(lst, index, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value and the value.
    """
#    print(lst)
    return max(lst, key=lst.count)[index][value]

def get_value_with_value_and_index(lst, value, index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value and the value.
    """
#    print(lst)
    return max(lst, key=lst.count)[index][value]

def get_value_with_value_and_index_and_value(lst, value, index, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value and the value.
    """
#    print(lst)
    return max(lst, key=lst.count)[index][value][index]

def get_value_with_index_and_value_and_value(lst, index