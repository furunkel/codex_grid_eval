
def some_func(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(text, key=lambda x: x[2])[1]

print(some_func(text))

# Output:
# ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')

# Explanation:
# The tuple with the largest third value is ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')
# The twelfth value of this tuple is 'l'