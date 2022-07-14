def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with a minus and False otherwise.
    """
    return text.translate(None, string.punctuation).lower() == string.punctuation.lower()


def remove_punctuation(text):
    """
    Remove punctuation from a string.
    """
    return text.translate(None, string.punctuation).lower()


def remove_non_ascii(text):
    """
    Remove non-ASCII characters from a string.
    """
    return text.translate(None, string.punctuation).encode('ascii', 'ignore')


def remove_non_ascii_chars(text):
    """
    Remove non-ASCII characters from a string.
    """
    return text.translate(None, string.punctuation).encode('ascii', 'ignore').decode('ascii')


def remove_non_ascii_chars_and_spaces(text):
    """
    Remove non-ASCII characters and spaces from a string.
    """
    return text.translate(None, string.punctuation).encode('ascii', 'ignore').decode('ascii').replace(' ', '')


def remove_non_ascii_chars_and_spaces_and_newlines(text):
    """
    Remove non-ASCII characters and spaces from a string.
    """
    return text.translate(None, string.punctuation).encode('ascii', 'ignore').decode('ascii').replace('\n', '')


def remove_non_ascii_chars_and_spaces_and_newlines_and_newlines(text):
    """
    Remove non-ASCII characters and spaces from a string.
    """
    return text.translate(None, string.punctuation).encode('ascii', 'ignore').decode('ascii').replace('\n', '')


def remove_non_ascii_chars_and_spaces_and_newlines_and_newlines(text):
    """
    Remove non-ASCII characters and spaces from a string.
    """
    return text.translate(None, string.punctuation).encode('ascii', 'ignore').decode('ascii').replace('\n', '')


def remove_non_ascii_chars_and_spaces_and_newlines_and_newlines(text):
    """
    Remove non-ASCII characters and spaces from a string.
    """
    return text.translate(None, string.punctuation).encode('ascii', 'ignore').decode('ascii').