
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest third value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def extract_value_with_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest third value.
    """
#    print(lst)
    return max(lst, key=lst.count)[-1]

def extract_value_with_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
#    print(lst)
    return min(lst, key=lst.count)[-1]

def extract_value_with_average(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the average third value.
    """
#    print(lst)
    return sum(lst)/len(lst)

def extract_value_with_variance(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the variance third value.
    """
#    print(lst)
    return variance(lst)/len(lst)

def extract_value_with_standard_deviation(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the standard deviation third value.
    """
#    print(lst)
    return std(lst)/len(lst)

def extract_value_with_standard_deviation_with_variance(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the standard deviation third value.
    """
#    print(lst)
    return std(lst)/len(lst)

def extract_value_with_variance_with_standard_deviation(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the standard deviation third value.
    """
#    print(lst)
    return std(lst)/len(lst)

def extract_value_with_standard_deviation_with_variance(lst):
    """
   