
def some_func(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest third value.
    """
    return max(text, key=lambda x: x[2])[1]

print(some_func([(1,2,3), (4,5,6), (7,8,9)]))

# Write a function that takes a list of numbers and returns the sum of the numbers.
def sum_func(nums):
    """
    Given a list of numbers, write a function that returns the sum of the numbers.
    """
    return sum(nums)

print(sum_func([1,2,3,4,5]))

# Write a function that takes a list of numbers and returns the largest number.
def largest_num(nums):
    """
    Given a list of numbers, write a function that returns the largest number.
    """
    return max(nums)

print(largest_num([1,2,3,4,5]))

# Write a function that takes a list of numbers and returns the smallest number.
def smallest_num(nums):
    """
    Given a list of numbers, write a function that returns the smallest number.
    """
    return min(nums)

print(smallest_num([1,2,3,4,5]))

# Write a function that takes a list of numbers and returns the second largest number.
def second_largest(nums):
    """
    Given a list of numbers, write a function that returns the second largest number.
    """
    return sorted(nums)[-2]

print(second_largest([1,2,3,4,5]))

# Write a function that takes a list of numbers and returns True if the list contains a 5.
def contains_five(nums):
    """
    Given a list of numbers, write a function that returns True if the list contains a 5.
    """
    return 5 in nums

print(contains_five([1,2,3,4,5]))

# Write a function that takes a list of numbers and returns True if the list contains a 5 and a 7.
def contains_five_seven(nums):
    """
    Given a list of numbers, write a function that returns True if the list contains a 5 and