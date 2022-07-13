
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
#    print(lst)
    twelfth = max(lst)[0]
    return twelfth

def max_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
#    print(lst)
    twelfth = min(lst)[0]
    return twelfth

def min_max_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
#    print(lst)
    twelfth = max_min(lst)[0]
    return twelfth

def max_min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
#    print(lst)
    twelfth = min_max(lst)[0]
    return twelfth

def min_max_min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
#    print(lst)
    twelfth = min_max_min(lst)[0]
    return twelfth

def max_min_max_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
#    print(lst)
    twelfth = min_max_min(lst)[0]
    return twelfth

def min_max_min_max_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
#    print(lst)
    twelfth = min_max_min_max(lst)[0]
    return twelfth
