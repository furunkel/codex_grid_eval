
def some_func(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[1]

print(some_func([(1,2,3), (4,5,6), (7,8,9)]))

# Write a function that takes a list of numbers and returns the sum of the numbers.

def sum_func(numbers):
    """
    Given a list of numbers, write a function that returns the sum of the numbers.
    """
    return sum(numbers)

print(sum_func([1,2,3,4,5]))

# Write a function that takes a list of numbers and returns the largest number in the list.

def largest_num(numbers):
    """
    Given a list of numbers, write a function that returns the largest number in the list.
    """
    return max(numbers)

print(largest_num([1,2,3,4,5]))

# Write a function that takes a list of words and returns the length of the longest word in the list.

def longest_word(words):
    """
    Given a list of words, write a function that returns the length of the longest word in the list.
    """
    return max(words, key=len)

print(longest_word(['hello', 'world', 'this', 'is', 'a', 'test']))

# Write a function that takes a list of numbers and returns a new list of all the numbers from the original list that are greater than their adjacent values.

def greater_than_adjacent(numbers):
    """
    Given a list of numbers, write a function that returns a new list of all the numbers from the original list that are greater than their adjacent values.
    """
    return [numbers[i] for i in range(1, len(numbers) - 1) if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]]

print(greater_than_adjacent([1,2,3,4,5,6,7,8,9]))

# Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list. Hint