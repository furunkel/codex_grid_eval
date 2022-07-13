
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with two underscores and True otherwise.
    """

def get_words(text):
    """
    Return a list of lowercase words in the given text.
    """
    return [word.lower() for word in text.split()]

def get_unique_words(text):
    """
    Return a list of unique words in the given text.
    """
    return [word for word in text.split() if word not in unique_words]

def get_unique_words_with_length(text):
    """
    Return a list of unique words in the given text, with the number of unique words in the given text.
    """
    return [word for word in text.split() if len(word) == len(unique_words)]

def get_unique_words_with_length_and_unique_words(text):
    """
    Return a list of unique words in the given text, with the number of unique words in the given text and the number of unique words in the given text.
    """
    return [word for word in text.split() if len(word) == len(unique_words) and unique_words.count(word) == 1]

def get_unique_words_with_length_and_unique_words_with_unique_words(text):
    """
    Return a list of unique words in the given text, with the number of unique words in the given text and the number of unique words in the given text.
    """
    return [word for word in text.split() if len(word) == len(unique_words) and unique_words.count(word) == 1 and unique_words.count(word) == 0]

def get_unique_words_with_length_and_unique_words_with_unique_words_with_unique_words(text):
    """
    Return a list of unique words in the given text, with the number of unique words in the given text and the number of unique words in the given text.
    """
    return [word for word in text.split() if len(word) == len(unique_words) and unique_words.count(word) == 1 and unique_words.count(word) == 0]

def get_unique