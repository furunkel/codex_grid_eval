
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst)[1]

# Write a function that takes a list as input and returns the number of tuples with second value less than or equal to 5.
def count_less_than_5(lst):
    """
    Given a list of tuples, write a function that returns the number of tuples with second value less than or equal to 5.
    """
    return len([x for x in lst if x[1]<=5])

# Write a function that takes a list as input and returns the number of tuples with second value greater than or equal to 5.
def count_greater_than_5(lst):
    """
    Given a list of tuples, write a function that returns the number of tuples with second value greater than or equal to 5.
    """
    return len([x for x in lst if x[1]>=5])

# Write a function that takes a list as input and returns the number of tuples with second value equal to 5.
def count_equal_5(lst):
    """
    Given a list of tuples, write a function that returns the number of tuples with second value equal to 5.
    """
    return len([x for x in lst if x[1]==5])

# Write a function that takes a list as input and returns the number of tuples with second value greater than or equal to 1.
def count_greater_than_1(lst):
    """
    Given a list of tuples, write a function that returns the number of tuples with second value greater than or equal to 1.
    """
    return len([x for x in lst if x[1]>1])

# Write a function that takes a list as input and returns the number of tuples with second value equal to 1.
def count_equal_1(lst):
    """
    Given a list of tuples, write a function that returns the number of tuples with second value equal to 1.
    """
    return len([x for x in lst if x[1]==1])

# Write a function that takes a list as input and returns the number of tuples with second value less than or equal to 0.
def count_less_than_0(lst):
    """
    Given a list of tuples, write a function that returns the number of tuples with second value less than or equal to 0.
    """
    return len([x for x in lst if x[1]<0])

# Write a function that takes a list as input and returns the number of tuples with second value equal to 0.
def count_equal_0(lst):
    """
    Given a list of tuples, write a function that returns the number of tuples with second value equal to 0.
    """
    return len([x for x in lst if x[1]==0])

# Write a function that takes a list as input and returns the number of tuples with second value greater than or equal to 0.
def count_greater_than_0(lst):
    """
    Given a list of tuples, write a function that returns the number of tuples with second value greater than or equal to 0.
    """
    return len([x for x in lst if x[1]>0])

# Write a function that takes a list as input and returns the number of tuples with second value less than or equal to 1.
def count_less_than_1(lst):
    """
    Given a list of tuples, write a function that returns the number of 