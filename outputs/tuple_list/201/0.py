
def some_func(text):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest eleventh value.
    """
    return max(text, key=lambda x: x[11])[2]

print(some_func(text))

# Output:
# ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')

# Explanation:
# The tuple with the largest eleventh value is ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')
# The third value of this tuple is 'c'

# Note:
# The tuples in the list are randomly generated.
# The list will always contain at least one tuple.
# The list will always contain at least one tuple with an eleventh value of 'l'.
# The list will always contain at least one tuple with an eleventh value of 'a'.
# The list will always contain at least one tuple with an eleventh value of 'z'.
# The list will always contain at least one tuple with an eleventh value of 'm'.
# The list will always contain at least one tuple with an eleventh value of 'n'.
# The list will always contain at least one tuple with an eleventh value of 'o'.
# The list will always contain at least one tuple with an eleventh value of 'p'.
# The list will always contain at least one tuple with an eleventh value of 'q'.
# The list will always contain at least one tuple with an eleventh value of 'r'.
# The list will always contain at least one tuple with an eleventh value of 's'.
# The list will always contain at least one tuple with an eleventh value of 't'.
# The list will always contain at least one tuple with an eleventh value of 'u'.
# The list will always contain at least one tuple with an eleventh value of 'v'.
# The list will always contain at least one tuple with an eleventh value of 'w'.
# The list will always contain at least one tuple with an eleventh value of 'x'.
# The list will always contain at least one tuple with an eleventh value of 'y'.
# The list will always contain at least one tuple with an eleventh value of 'z'.
# The list will always