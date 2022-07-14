def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with two underscores and True otherwise.
    """
    return text.replace(' ', '_')


def get_unique_words(text):
    """
    Return a list of unique words found in the text.
    """
    return [word for word in text.split() if word not in STOPWORDS]


def get_unique_words_with_counts(text):
    """
    Return a list of unique words found in the text.
    """
    return [word for word in text.split() if word not in STOPWORDS and word not in STOPWORDS_WITH_DUPLICATE]


def get_unique_words_with_counts_and_counts(text):
    """
    Return a list of unique words found in the text.
    """
    return [word for word in text.split() if word not in STOPWORDS and word not in STOPWORDS_WITH_DUPLICATE and word not in STOPWORDS_WITH_DUPLICATE_AND_DUPLICATE]


def get_unique_words_with_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_counts_and_