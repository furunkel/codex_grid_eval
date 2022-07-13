
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def tuple_extract_with_last(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
#    print(lst)
    return max(lst, key=lst.count)[-1]

def tuple_extract_with_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
#    print(lst)
    return min(lst, key=lst.count)[0]

def tuple_extract_with_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value and the first value.
    """
#    print(lst)
    return max(lst, key=lst.count)[-1], lst[0]

def tuple_extract_with_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value and the first value.
    """
#    print(lst)
    return min(lst, key=lst.count)[0], lst[0]

def tuple_extract_with_first_and_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value and the first value.
    """
#    print(lst)
    return min(lst, key=lst.count)[-1], lst[0]

def tuple_extract_with_first_and_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value and the first value.
    """
#    print(lst)
    return min(lst, key=lst.count)[-1], lst[0]

def tuple_extract_with_first_and_last_and_first_and_last(lst):
    """
    Given