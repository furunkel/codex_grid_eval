
def f(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[0]

print(f([(1,7), (1,3), (3,4,5), (2,2)]))

# 2.
def f(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
    return max(text, key=lambda x: x[0])[1]

print(f([(1,3), (1,7), (3,4,5), (2,2)]))

# 3.
def f(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[1]

print(f([(1,3), (1,7), (3,4,5), (2,2)]))

# 4.
def f(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[0]

print(f([(1,7), (1,3), (3,4,5), (2,2)]))

# 5.
def f(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[1]

print(f([(1,3), (1,7), (3,4,5), (2,2)]))

# 6.
def f(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[1]

print(f([(1,3), (1,7), (3,4,5), (2,2)]))

# 7.
def f(