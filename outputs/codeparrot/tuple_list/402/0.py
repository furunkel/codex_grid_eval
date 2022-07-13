
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
#    print lst
    if len(lst) == 0:
        return None
    return max(lst, key=lambda x: x[1])[0]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return min(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return sum(lst)/len(lst)

def get_value_from_list_with_variance(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return sum(lst)/len(lst)

def get_value_from_list_with_std(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return math.sqrt(sum(lst)/len(lst))

def get_value_from_list_with_