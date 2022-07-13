
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value.
    """
#    print(lst)
    if len(lst) == 0:
        return 0
    return min(lst, key=lambda x: x[1])[0]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value.
    """
#    print(lst)
    if len(lst) == 0:
        return 0
    return max(lst, key=lambda x: x[1])[0]

def get_value_with_twelfth(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value.
    """
#    print(lst)
    if len(lst) == 0:
        return 0
    return max(lst, key=lambda x: x[1])[0]

def get_value_with_twelfth_and_twelfth(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value and the smallest twelfth value.
    """
#    print(lst)
    if len(lst) == 0:
        return 0
    return max(lst, key=lambda x: x[1])[0], max(lst, key=lambda x: x[1])[1]

def get_value_with_twelfth_and_twelfth_and_twelfth(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value and the smallest twelfth value and the smallest twelfth value.
    """
#    print(lst)
    if len(lst) == 0:
        return 0
    return max(lst, key=lambda x: x[1])[0], max(lst, key=lambda x: x[1])[1], max(lst, key=lambda x: x[1])[2]

def get_value_with_twelf