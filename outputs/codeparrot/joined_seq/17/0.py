def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with two underscores and False otherwise.
    """
    return ''.join([c for c in text if c.isalpha() or c.isdigit()])


def get_words(text):
    """
    Return a list of lowercase words found in the given text.
    """
    return [w for w in text.split() if w.isalpha()]


def get_unique_words(text):
    """
    Return a list of unique words found in the given text.
    """
    return [w for w in text.split() if w.isalpha()]


def get_unique_words_with_counts(text):
    """
    Return a list of unique words found in the given text, with counts.
    """
    return [w for w in text.split() if w.isalpha()]


def get_unique_words_with_counts_and_counts(text):
    """
    Return a list of unique words found in the given text, with counts and counts.
    """
    return [w for w in text.split() if w.isalpha()]


def get_unique_words_with_counts_and_counts_and_counts_and_counts(text):
    """
    Return a list of unique words found in the given text, with counts and counts and counts and counts and counts and counts and counts and counts and counts and counts.
    """
    return [w for w in text.split() if w.isalpha()]


def get_unique_words_with_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts(text):
    """
    Return a list of unique words found in the given text, with counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and counts and