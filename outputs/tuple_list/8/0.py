
def f(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest first value.
    """
    return max(text, key=lambda x: x[0])[0]

print(f([(1,2), (3,4), (5,6)]))

# 2.
def f(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[0]

print(f([(1,2), (3,4), (5,6)]))

# 3.
def f(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
    return max(text, key=lambda x: x[0])[1]

print(f([(1,2), (3,4), (5,6)]))

# 4.
def f(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[1]

print(f([(1,2), (3,4), (5,6)]))

# 5.
def f(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[0]

print(f([(1,2), (3,4), (5,6)]))

# 6.
def f(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[0]

print(f([(1,2), (3,4), (5,6)]))

# 7.
def f(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(text, key