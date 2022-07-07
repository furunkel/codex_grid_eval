
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest last value.
    """
    return max(text, key=lambda x: x[-1])[-1]


def extract_min_max(text):
    """
    Given a list of tuples, write a function that returns a tuple with the lowest value in index 0 and the highest
    value in index 1.
    """
    return min(text, key=lambda x: x[0])[0], max(text, key=lambda x: x[1])[1]


def swap_chars(text):
    """
    Given a string of characters, write a function that returns the string with the first and last characters swapped.
    """
    return text[-1] + text[1:-1] + text[0]


def reverse_string(text):
    """
    Given a string of characters, write a function that returns the string reversed.
    """
    return text[::-1]


def sort_by_word_length(text):
    """
    Given a list of words, write a function that returns a list of tuples where the first item is the length of the
    word and the second item is the word.
    """
    return sorted(text, key=lambda x: len(x))


def sort_by_last_letter(text):
    """
    Given a list of words, write a function that returns a list of tuples where the first item is the last letter of
    the word and the second item is the word.
    """
    return sorted(text, key=lambda x: x[-1])


def sort_by_word_and_num_of_vowels(text):
    """
    Given a list of words, write a function that returns a list of tuples where the first item is the number of vowels
    in the word and the second item is the word.
    """
    return sorted(text, key=lambda x: (len(re.findall(r'[aeiou]', x, re.I)), x))


def sort_by_num_of_vowels(text):
    """
    Given a list of words, write a function that returns a list of tuples where the first item is the number of vowels
    in the word and