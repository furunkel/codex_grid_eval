
def some_func(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(text, key=lambda x: x[2])[-1]

print(some_func([(10, 20, 40), (40, 50, 15), (20, 35, 17)]))

# Output: 17

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of strings and returns a single string that is an HTML unordered list
# (<ul>...</ul>) of those strings. You should include a newline ('\n') between each string in the list.

def some_func(text):
    """
    Write a function that takes a list of strings and returns a single string that is an HTML unordered list
    (<ul>...</ul>) of those strings. You should include a newline ('\n') between each string in the list.
    """
    return '<ul>\n' + '\n'.join(['<li>{}</li>'.format(x) for x in text]) + '\n</ul>'

print(some_func(['first string', 'second string']))

# Output:
# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a function that takes a list of strings and returns a single string that is an HTML unordered list
# (<ul>...</ul>) of those strings. You should include a newline ('\n') between each string in the list.

def some_func(text):
    """
    Write a function that takes a list of strings and returns a single string that is an HTML unordered list
    (<ul>...</ul>) of those strings. You should include a newline ('\n') between each string in the list.
    """
    return '<ul>\n' + '\n'.join(['<li>{}</li>'.format(x) for x in text]) + '\n</ul>'

print(some_func(['first string', 'second string']))

# Output:
# <ul>
# <li>first string</li>
# <li>second string</li>
# </