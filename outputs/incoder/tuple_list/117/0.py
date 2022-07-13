
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda t: t[2])[2]


# Test Cases
# ---------
# Write a test case for each of the following inputs:
# - A list with three tuples
# - A list with one tuple
# - A list with two tuples
# - A list with one tuple and one element
# - A list with two tuples and one element
# - A list with three tuples and one element
# - A list with one tuple, one element, and one element
# - A list with two tuples, one element, and one element
# - A list with three tuples, one element, and one element
# - A list with one tuple, one element, and two elements
# - A list with two tuples, one element, and two elements
# - A list with three tuples, one element, and two elements
# - A list with one tuple, one element, and three elements
# - A list with two tuples, one element, and three elements
# - A list with three tuples, one element, and three elements
# - A list with one tuple, two elements, and one element
# - A list with two tuples, two elements, and one element
# - A list with three tuples, two elements, and one element
# - A list with one tuple, two elements, and two elements
# - A list with two tuples, two elements, and two elements
# - A list with three tuples, two elements, and two elements
# - A list with one tuple, two elements, and three elements
# - A list with two tuples, two elements, and three elements
# - A list with three tuples, two elements, and three elements
# - A list with one tuple, three elements, and one element
# - A list with two tuples, three elements, and one element
# - A list with three tuples, three elements, and one element
# - A list with one tuple, three elements, and two elements
# - A list with two tuples, three elements, and two elements
# - A list with three tuples, three elements, and two elements
# - A list with one tuple, three elements, and three elements
# - A list with two tuples, three elements, and three elements
# - A list with three tuples, three elements, and three elements
# - A list with one tuple, four elements, and one element
# - A list with two tuples, four elements, and one element
# - A list with three tuples, four elements, and one element
# - A list with one tuple, four elements, and two elements
# - 