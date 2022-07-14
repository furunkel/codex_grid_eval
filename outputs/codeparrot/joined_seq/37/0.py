def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with a plus and True otherwise.
    """
    return text.translate(None, string.punctuation).replace(" ", "")


def get_words(text):
    """
    Return a list of words in the given text.
    """
    return [word.lower() for word in text.split()]


def get_sentences(text):
    """
    Return a list of sentences in the given text.
    """
    return [sentence.strip() for sentence in text.split("\n")]


def get_sentences_with_punctuation(text):
    """
    Return a list of sentences in the given text, with punctuation removed.
    """
    return [sentence.strip() for sentence in text.split(" ") if sentence.strip()]


def get_sentences_with_punctuation_and_punctuation(text):
    """
    Return a list of sentences in the given text, with punctuation removed and punctuation removed.
    """
    return [sentence.strip() for sentence in text.split(" ") if sentence.strip() and sentence.strip() not in string.punctuation]


def get_sentences_with_punctuation_and_punctuation_and_punctuation_and_punctuation(text):
    """
    Return a list of sentences in the given text, with punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed