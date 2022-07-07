
def some_func(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[0]

print(some_func([(1,2), (3,4), (5,6)]))

# Write a function that returns the sum of all the values in a dictionary.
def some_func(text):
    """
    Write a function that returns the sum of all the values in a dictionary.
    """
    return sum(text.values())

print(some_func({'a': 1, 'b': 2, 'c': 3}))

# Write a function that takes a list of numbers and returns the largest number in the list.
def some_func(text):
    """
    Write a function that takes a list of numbers and returns the largest number in the list.
    """
    return max(text)

print(some_func([1,2,3,4,5]))

# Write a function that takes a list of numbers and returns the smallest number in the list.
def some_func(text):
    """
    Write a function that takes a list of numbers and returns the smallest number in the list.
    """
    return min(text)

print(some_func([1,2,3,4,5]))

# Write a function that takes a list of strings and returns a single string that is an HTML unordered list (<ul>...</ul>) of those strings. You should include a brief explanation of your code.
def some_func(text):
    """
    Write a function that takes a list of strings and returns a single string that is an HTML unordered list (<ul>...</ul>) of those strings. You should include a brief explanation of your code.
    """
    return '<ul>\n' + '\n'.join(['<li>{}</li>'.format(x) for x in text]) + '\n</ul>'

print(some_func(['a', 'b', 'c']))

# Write a function that takes a list of strings and a target string. Return True if the target string is in the list, False if it is not.
def some_func(text, target):
    """
    Write a function that takes a list of strings and a