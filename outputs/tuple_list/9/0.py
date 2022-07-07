
def some_func(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest first value.
    """
    return max(text, key=lambda x: x[0])[0]

print(some_func([(1,2), (10,20), (100,0)]))

# Write a function that takes a list of numbers and returns True if there is an even number of even numbers.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True if there is an even number of even numbers.
    """
    return len([x for x in text if x % 2 == 0]) % 2 == 0

print(some_func([5,6,2]))
print(some_func([5,5,2]))

# Write a function that takes a list of numbers and returns True if every number is even.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True if every number is even.
    """
    return all([x % 2 == 0 for x in text])

print(some_func([2,6,18,10]))
print(some_func([2,6,18,11]))

# Write a function that takes a list of numbers and returns True if some number is even.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True if some number is even.
    """
    return any([x % 2 == 0 for x in text])

print(some_func([1,3,5]))
print(some_func([1,4,5]))

# Write a function that takes a list of numbers and returns True if some number is odd.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True if some number is odd.
    """
    return any([x % 2 != 0 for x in text])

print(some_func([2,4,6,8]))
print(some_func([2,4,6,7]))

# Write a function that takes a list of numbers and returns True if every number is odd.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True