
def some_func(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
    """
    return max(text, key=lambda x: x[0])[1]

print(some_func([(1,2), (10, 20), (100, 200), (1000, 2000)]))

# Output: 2000

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list.
# Hint: Use slicing and a for loop.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list.
    """
    for i in range(len(text)):
        if text[i:i+3] == [1,2,3]:
            return True
    return False

print(some_func([1,2,3,4,5,6,7,8,9]))
print(some_func([1,2,4,5,6,7,8,9]))

# Output:
# True
# False

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list.
# Hint: Use slicing and a for loop.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list.
    """
    for i in range(len(text)):
        if text[i:i+3] == [1,2,3]:
            return True
    return False

print(some_func([1,2,3,4,5,6,7,8,9]))
print(some_func([1,2,4,5,6,7,8,9]))

# Output:
# True
# False

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list.
# Hint: Use slicing and a for loop.

def some