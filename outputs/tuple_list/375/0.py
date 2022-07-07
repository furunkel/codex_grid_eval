
def some_func(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[-1]

print(some_func([(1,2), (4,1), (9,10), (13,-3)]))

# Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list. Hint: Use slicing and a for loop.

def some_func(text):
    """
    Write a function that takes a list of numbers and returns True if the sequence [1,2,3] is somewhere in the list. Hint: Use slicing and a for loop.
    """
    for i in range(len(text)):
        if text[i:i+3] == [1,2,3]:
            return True
    return False

print(some_func([1,2,3,4,5,6,7,8,9,10]))

# Write a function that takes a list of strings an prints them, one per line, in a rectangular frame. For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:

def some_func(text):
    """
    Write a function that takes a list of strings an prints them, one per line, in a rectangular frame. For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:
    """
    max_len = max(len(i) for i in text)
    print('*' * (max_len + 4))
    for i in text:
        print('* ' + i + ' ' * (max_len - len(i)) + ' *')
    print('*' * (max_len + 4))

some_func(["Hello", "World", "in", "a", "frame"])

# Write function that translates a text to Pig Latin and back. English is translated to Pig Latin by taking the first letter of every word, moving it to the end of the word and adding 'ay'. "The quick brown fox" becomes "Hetay uickqay rownbay oxfay".

def some_func(text):
    """
    Write function that translates a text to Pig Latin and back