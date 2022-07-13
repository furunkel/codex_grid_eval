
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
#    print lst
    return max(lst, key=lst.count)

def fibonacci_with_max(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
#    print lst
    return max(lst, key=lst.count)

def fibonacci_with_min(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
#    print lst
    return min(lst, key=lst.count)

def fibonacci_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum of the values of the tuple with the largest twelfth value.
    """
#    print lst
    return sum(lst, key=lst.count)

def fibonacci_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the mean of the values of the tuple with the largest twelfth value.
    """
#    print lst
    return sum(lst, key=lst.count) / float(len(lst))

def fibonacci_with_std(lst):
    """
    Given a list of tuples, write a function that returns the standard deviation of the values of the tuple with the largest twelfth value.
    """
#    print lst
    return math.sqrt(sum(lst, key=lst.count)) / float(len(lst))

def fibonacci_with_var(lst):
    """
    Given a list of tuples, write a function that returns the variance of the values of the tuple with the largest twelfth value.
    """
#    print lst
    return math.sqrt(sum(lst, key=lst.count)) / float(len(lst))

def fibonacci_with_median(lst):
    """
    Given a list of tuples, write a function that returns the median of the values of the tuple with