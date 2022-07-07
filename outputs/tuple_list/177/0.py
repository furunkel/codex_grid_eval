
def some_func(text):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest third value.
    """
    return max(text, key=lambda x: x[2])[2]

print(some_func([(1,2,3), (4,5,6), (7,8,9)]))

# Write a function that takes a list of numbers and returns the largest number in the list.

def some_func(text):
    """
    Given a list of numbers, write a function that returns the largest number in the list.
    """
    return max(text)

print(some_func([1,2,3,4,5,6,7,8,9]))

# Write a function that takes a list of numbers and returns the smallest number in the list.

def some_func(text):
    """
    Given a list of numbers, write a function that returns the smallest number in the list.
    """
    return min(text)

print(some_func([1,2,3,4,5,6,7,8,9]))

# Write a function that takes a list of numbers and returns True if the sequence contains an even number of even numbers.

def some_func(text):
    """
    Given a list of numbers, write a function that returns True if the sequence contains an even number of even numbers.
    """
    even_count = 0
    for i in text:
        if i % 2 == 0:
            even_count += 1
    return even_count % 2 == 0

print(some_func([5, 6, 2]))
print(some_func([5, 5, 2]))

# Write a function that takes a list of numbers and returns True if the sequence contains an odd number of odd numbers.

def some_func(text):
    """
    Given a list of numbers, write a function that returns True if the sequence contains an odd number of odd numbers.
    """
    odd_count = 0
    for i in text:
        if i % 2 != 0:
            odd_count += 1
    return odd_count % 2 != 0

print(some_func([5, 6, 2]))
print(some_func([5, 5, 2]))

# Write a function that takes a list of numbers and