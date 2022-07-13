
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
#    print(lst)
    if len(lst) == 0:
        return 0
    return max(lst, key=lambda x: x[1])[0]

def get_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[1])[1]

def get_value_from_list_with_avg(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
    return sum(lst)/len(lst)

def get_value_from_list_with_std(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
    return math.sqrt(sum(lst)/len(lst))

def get_value_from_list_with_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value.
    """
   