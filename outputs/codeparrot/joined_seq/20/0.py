def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with a minus and False otherwise.
    """
    return text.upper().replace(' ', '') == text


def get_all_words(text):
    """
    Return a list of all words in the given text.
    """
    return [word for word in text.split() if word not in STOPWORDS]


def get_all_sentences(text):
    """
    Return a list of all sentences in the given text.
    """
    return [sentence for sentence in text.split() if sentence not in SENTENCES]


def get_all_sentences_with_punctuation(text):
    """
    Return a list of all sentences in the given text, with punctuation removed.
    """
    return [sentence for sentence in text.split() if sentence not in PUNCTUATION_PUNCTUATION]


def get_all_sentences_with_punctuation_and_punctuation_removed(text):
    """
    Return a list of all sentences in the given text, with punctuation removed.
    """
    return [sentence for sentence in text.split() if sentence not in PUNCTUATION_PUNCTUATION_AND_PUNCTUATION_PUNCTUATION]


def get_all_sentences_with_punctuation_and_punctuation_removed_and_punctuation(text):
    """
    Return a list of all sentences in the given text, with punctuation removed and punctuation removed.
    """
    return [sentence for sentence in text.split() if sentence not in PUNCTUATION_PUNCTUATION_AND_PUNCTUATION_PUNCTUATION_PUNCTUATION]


def get_all_sentences_with_punctuation_and_punctuation_removed_and_punctuation_and_punctuation(text):
    """
    Return a list of all sentences in the given text, with punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and punctuation removed and