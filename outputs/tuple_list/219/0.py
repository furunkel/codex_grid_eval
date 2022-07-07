
def some_func(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[1]

print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10)]))

# Output: 2

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of tuples and returns a list of tuples where the first value is the second value of the input tuple.

def some_func(text):
    """
    Write a function that takes a list of tuples and returns a list of tuples where the first value is the second value of the input tuple.
    """
    return [(x[1], x[0]) for x in text]

print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10)]))

# Output: [(2, 1), (4, 3), (6, 5), (8, 7), (10, 9)]

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of tuples and returns a list of tuples where the first value is the second value of the input tuple.

def some_func(text):
    """
    Write a function that takes a list of tuples and returns a list of tuples where the first value is the second value of the input tuple.
    """
    return [(x[1], x[0]) for x in text]

print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10)]))

# Output: [(2, 1), (4, 3), (6, 5), (8, 7), (10, 9)]

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of tuples and returns a list of tuples where the first value is the second value of the input tuple.

def some_func(text):
    """
    Write a function that takes a list of tuples and returns a list of tuples where the first value is the second value of the input tuple.
    """
    return [(x[1], x[0]) for x in text]
