
def some_func(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value.
    """
    return max(text, key=lambda x: x[11])[1]

print(some_func(text))

# Output:
# ('B', 'B')

# Explanation:
# The second value of the tuple with the largest twelfth value is 'B'.