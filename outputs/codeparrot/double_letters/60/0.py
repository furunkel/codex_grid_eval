def double_letters(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    return "".join([c for c in string if c.isalpha()])


def get_words(text):
    """
    Given a string, return a list of words.
    """
    return [w for w in re.split(r"\s+", text) if w]


def get_sentences(text):
    """
    Given a string, return a list of sentences.
    """
    return [s for s in re.split(r"\s+", text) if s]


def get_sentences_with_offsets(text):
    """
    Given a string, return a list of sentences, where each sentence is a list of tuples (word, offset).
    """
    return [s for s in re.split(r"\s+", text) if s]


def get_sentences_with_offsets_and_sentences(text):
    """
    Given a string, return a list of sentences, where each sentence is a list of tuples (word, offset, sentence).
    """
    return [s for s in re.split(r"\s+", text) if s]


def get_sentences_with_offsets_and_sentences_with_offsets(text):
    """
    Given a string, return a list of sentences, where each sentence is a list of tuples (word, offset, sentence).
    """
    return [s for s in re.split(r"\s+", text) if s]


def get_sentences_with_offsets_and_sentences_with_offsets_and_sentences(text):
    """
    Given a string, return a list of sentences, where each sentence is a list of tuples (word, offset, sentence).
    """
    return [s for s in re.split(r"\s+", text) if s]


def get_sentences_with_offsets_and_sentences_with_offsets_and_sentences_with_offsets(text):
    """
    Given a string, return a list of sentences, where each sentence is a list of tuples (word, offset, sentence).
    """
    return [s for s in re.split(r"\s+", text