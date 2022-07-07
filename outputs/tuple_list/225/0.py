
def some_func(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(text, key=lambda x: x[0])[1]

print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10)]))

# Output: 10

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of numbers and returns the largest number in the list.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns the largest number in the list.
    """
    return max(text)

print(some_func([1,2,3,4,5,6,7,8,9,10]))

# Output: 10

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of numbers and returns the smallest number in the list.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns the smallest number in the list.
    """
    return min(text)

print(some_func([1,2,3,4,5,6,7,8,9,10]))

# Output: 1

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of numbers and returns the average of the numbers.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns the average of the numbers.
    """
    return sum(text) / len(text)

print(some_func([1,2,3,4,5,6,7,8,9,10]))

# Output: 5.5

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of numbers and returns the median of the numbers.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns the median of the numbers.
    """
    text.sort()
    if len(text) % 2 == 0:
        return (text[len(text) // 2] + text[len(text) // 2 - 1]) / 2
    else:
        return text[len(