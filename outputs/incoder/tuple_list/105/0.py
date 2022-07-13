
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest third value.
    """
    return max(lst, key=lambda tup: tup[2])[1]


# Test Cases
# ---------
# Write a test case for each of the above functions.
# Your test cases should follow the following format. Your test cases should be
# similar to the following block of code. Make sure you follow the indentation and
# spacing rules.
# Input:
# Output:
# Notes:
# - Test cases follow the same format as the example above.

# Test Case 1
# Input:
# lst = [(1, 2), (3, 4), (-1, -2), (1, -2), (-1, 2)]
# Output: 4
# Explanation: Your function should return 4 since it is the second element in the tuple with the largest third value.

# Test Case 2
# Input:
# lst = [(1, 2), (3, 4), (-1, -2), (1, -2), (-1, 2), (1, 3), (2, 3)]
# Output: 3
# Explanation: Your function should return 3 since it is the second element in the tuple with the largest third value.

# Test Case 3
# Input:
# lst = [(1, 2), (3, 4), (-1, -2), (1, -2), (-1, 2), (1, 3), (2, 3)]
# Output: 3
# Explanation: Your function should return 3 since it is the second element in the tuple with the largest third value.

# Test Case 4
# Input:
# lst = [(1, 2), (3, 4), (-1, -2), (1, -2), (-1, 2), (1, 3), (2, 3)]
# Output: 3
# Explanation: Your function should return 3 since it is the second element in the tuple with the largest third value.

# Test Case 5
# Input:
# lst = [(1, 2), (3, 4), (-1, -2), (1, -2), (-1, 2), (1, 3), (2, 3)]
# Output: 3
# Explanation: Your function should return 3 since it is the second element in the tuple with the largest third value.

# Test Case 6
# Input:
# lst = [(1, 2), (3, 4), (-1, -2), (1, -2), (-1, 2), (1, 3), (2, 3)]
# Output: 3
# Explanation: Your function should return 3 since it is the second element in the tuple with the largest third value.

# Test Case 7
# Input:
# lst = [(1, 2), (3, 4), (-1, -2), (1, -2), (-1, 2), (1, 3), (2, 3)]
# Output: 3
# Explanation: Your function should return 3 since it is the second element in the tuple with the largest third value.

# Test Case 8
# Input:
# lst = [(1, 2), (3, 4), (-1, -2), (1, -2), (-1, 2), (1, 3), (2, 3)]
# Output: 3
# 