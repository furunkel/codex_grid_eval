
def some_func(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[1]

print(some_func([(1,2), (3,4), (5,6)]))

# Write a function that takes a list of numbers and returns the largest number in the list.

def some_func(text):
    """
    Given a list of numbers, write a function that returns the largest number in the list.
    """
    return max(text)

print(some_func([1,2,3,4,5,6]))

# Write a function that takes a list of numbers and returns the smallest number in the list.

def some_func(text):
    """
    Given a list of numbers, write a function that returns the smallest number in the list.
    """
    return min(text)

print(some_func([1,2,3,4,5,6]))

# Write a function that takes a list of numbers and returns the second largest number in the list.

def some_func(text):
    """
    Given a list of numbers, write a function that returns the second largest number in the list.
    """
    return sorted(text)[-2]

print(some_func([1,2,3,4,5,6]))

# Write a function that takes a list of numbers and returns the second smallest number in the list.

def some_func(text):
    """
    Given a list of numbers, write a function that returns the second smallest number in the list.
    """
    return sorted(text)[1]

print(some_func([1,2,3,4,5,6]))

# Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list. Hint: Use slicing and a for loop.

def some_func(text):
    """
    Given a list of numbers, write a function that returns True if the sequence [1,2,3] is somewhere in the list.
    """
    for i in range(len(text)):
        if text[i:i+3] == [1,2,3]:
            return True
    return