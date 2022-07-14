def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with a minus and True otherwise.
    """
    return text.translate(None, string.punctuation).lower() == string.punctuation.lower()


def get_words(text):
    """
    Return a list of words in the text.
    """
    return [word.lower() for word in text.split()]


def get_sentences(text):
    """
    Return a list of sentences in the text.
    """
    return [sentence.lower() for sentence in text.split()]


def get_sentences_with_punctuation(text):
    """
    Return a list of sentences in the text, with punctuation removed.
    """
    return [sentence.lower() for sentence in text.split() if sentence not in string.punctuation]


def get_sentences_with_punctuation_and_punctuation(text):
    """
    Return a list of sentences in the text, with punctuation removed and punctuation removed.
    """
    return [sentence.lower() for sentence in text.split() if sentence not in string.punctuation and sentence not in string.punctuation]


def get_sentences_with_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_punctuation_and_