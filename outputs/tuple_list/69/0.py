
def some_func(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest last value.
    """
    return max(text, key=lambda x: x[1])[0]

print(some_func([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))

# Output: (3, 4, 5)

# ----------------------------------------------------------------------------------------------------------------------

# Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list.
# Hint: Use slicing and a for loop.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list.
    """
    for i in range(len(text)):
        if text[i:i+3] == [1, 2, 3]:
            return True
    return False

print(some_func([1, 1, 2, 4, 1]))
print(some_func([1, 1, 2, 1, 2, 3]))
print(some_func([1, 1, 2, 1, 2, 1]))

# Output:
# False
# True
# False

# ----------------------------------------------------------------------------------------------------------------------

# Write a function that takes a list of numbers and returns True if the sequence of numbers 1, 2, 3 appears in the list
# somewhere.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True if the sequence of numbers 1, 2, 3 appears in the list
    somewhere.
    """
    for i in range(len(text)):
        if text[i:i+3] == [1, 2, 3]:
            return True
    return False

print(some_func([1, 1, 2, 4, 1]))
print(some_func([1, 1, 2, 1, 2, 3]))
print(some_func([1, 1, 2, 1, 2, 1]))

# Output:
# False
# True
# False

# ----------------------------------------------------------------------------------------------------------------------

# Write a function that takes a list of numbers and returns True if the sequence of numbers 1, 2, 3 appears in the list
# somewhere.

def some