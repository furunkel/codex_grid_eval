
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def extract_value_with_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count)

def extract_value_with_min(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lst.count)

def extract_value_with_avg(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
    return sum(lst)/len(lst)

def extract_value_with_std(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
    return math.sqrt(sum(lst)/len(lst))

def extract_value_with_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lst.count)

def extract_value_with_avg_and_std(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
    return math.sqrt(sum(lst)/len(lst))

def extract_value_with_std_and_min(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
    return math.sqrt(sum(lst)/len(lst))

def extract_value_with_min_and_max_and_avg(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest twe