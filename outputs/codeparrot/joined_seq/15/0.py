def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with an underscore and False otherwise.
    """
    return text.lower() in string.lowercase


def get_all_words(text):
    """
    Return a list of all words in the given text.
    """
    return [word for word in text.split() if word not in stopwords.words('english')]


def get_all_sentences(text):
    """
    Return a list of all sentences in the given text.
    """
    return [sentence for sentence in text.split() if sentence not in stopwords.words('english')]


def get_all_words_and_sentences(text):
    """
    Return a list of all words and sentences in the given text.
    """
    return [word for word in text.split() for sentence in get_all_sentences(text)]


def get_all_sentences_and_words(text):
    """
    Return a list of all sentences and words in the given text.
    """
    return [sentence for sentence in get_all_sentences(text)] + get_all_words(text)


def get_all_words_and_sentences_and_words(text):
    """
    Return a list of all words and sentences and words in the given text.
    """
    return [word for word in get_all_words_and_sentences(text)] + get_all_words_and_sentences(text) + get_all_sentences_and_words(text)


def get_all_sentences_and_words_and_sentences(text):
    """
    Return a list of all sentences and words in the given text.
    """
    return [sentence for sentence in get_all_sentences_and_words_and_sentences(text)] + get_all_words_and_sentences(text)


def get_all_words_and_sentences_and_words_and_sentences(text):
    """
    Return a list of all words and sentences and words in the given text.
    """
    return [word for word in get_all_words_and_sentences_and_words_and_sentences(text)] + get_all_words_and_sentences_and_words_and_sentences(text)


def get_all_sentences