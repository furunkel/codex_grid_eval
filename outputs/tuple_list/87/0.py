
def some_func(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[1]

print(some_func([(1,2), (3,4), (5,6)]))

# 2. Write a function that takes a list of numbers and returns the sum of the numbers.

def sum_func(numbers):
    """
    Given a list of numbers, write a function that returns the sum of the numbers.
    """
    return sum(numbers)

print(sum_func([1,2,3,4,5]))

# 3. Write a function that takes a list of numbers and returns the largest number in the list.

def largest_num(numbers):
    """
    Given a list of numbers, write a function that returns the largest number in the list.
    """
    return max(numbers)

print(largest_num([1,2,3,4,5]))

# 4. Write a function that takes a list of words and returns the length of the longest word in the list.

def longest_word(words):
    """
    Given a list of words, write a function that returns the length of the longest word in the list.
    """
    return max(words, key=len)

print(longest_word(['hello', 'world', 'this', 'is', 'a', 'test']))

# 5. Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.

def divide_by_two(numbers):
    """
    Given a list of numbers, write a function that returns a new list of all those numbers divided by two.
    """
    return [num / 2 for num in numbers]

print(divide_by_two([1,2,3,4,5]))

# 6. Write a function that takes a list of words and returns a list of all the lengths of those words.

def word_lengths(words):
    """
    Given a list of words, write a function that returns a list of all the lengths of those words.
    """
    return [len(word) for word in words]

print(word_lengths(['hello', 'world',