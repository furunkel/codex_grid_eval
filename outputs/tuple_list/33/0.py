
def some_func(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest third value.
    """
    return max(text, key=lambda x: x[2])[0]

print(some_func([(1,2,3), (4,5,6), (7,8,9)]))

# Write a function that takes a list of numbers and returns True if there is an even number of even numbers.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True if there is an even number of even numbers.
    """
    return len([x for x in text if x % 2 == 0]) % 2 == 0

print(some_func([5, 6, 2]))
print(some_func([5, 5, 2]))

# Write a function that accepts two lists both of which contain integers and returns a new list which contains all the elements from both lists.
# If the two lists have the same value at the same index, then the element from the first list should be used.

def some_func(text1, text2):
    """
    Write a function that accepts two lists both of which contain integers and returns a new list which contains all the elements from both lists.
    If the two lists have the same value at the same index, then the element from the first list should be used.
    """
    return [text1[x] if text1[x] != text2[x] else text2[x] for x in range(len(text1))]

print(some_func([1, 2, 3], [3, 2, 1]))

# Write a function that takes a list of integers and returns the average value.

def some_func(text):
    """
    Write a function that takes a list of integers and returns the average value.
    """
    return sum(text) / len(text)

print(some_func([1, 2, 3]))

# Write a function that takes a list of integers and returns True if the sequence [1,2,3] is somewhere in the list.

def some_func(text):
    """
    Write a function that takes a list of integers and returns True if the sequence [1,2,3] is somewhere in the list.
    """
    return [1, 2,