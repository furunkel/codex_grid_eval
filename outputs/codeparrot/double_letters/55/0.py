def double_letters(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return "".join([c for c in string if c.isupper()])


def get_words(text):
    """
    Given a string, return a list of words.
    """
    return [word.lower() for word in re.split(r"\s+", text) if word.isalpha()]


def get_sentences(text):
    """
    Given a string, return a list of sentences.
    """
    return [sentence.lower() for sentence in re.split(r"\s+", text) if sentence.isalpha()]


def get_sentences_with_length(text, length):
    """
    Given a string, return a list of sentences, where each sentence is a list of words.
    """
    return [sentence.lower() for sentence in re.split(r"\s+", text) if sentence.isalpha() and len(sentence) >= length]


def get_sentences_with_length_and_sentences(text, length, sentences):
    """
    Given a string, return a list of sentences, where each sentence is a list of words.
    """
    return [sentence.lower() for sentence in sentences if len(sentence) >= length]


def get_sentences_with_length_and_sentences_with_length(text, length, sentences):
    """
    Given a string, return a list of sentences, where each sentence is a list of words.
    """
    return [sentence.lower() for sentence in sentences if len(sentence) >= length]


def get_sentences_with_length_and_sentences_with_length_and_sentences(text, length, sentences):
    """
    Given a string, return a list of sentences, where each sentence is a list of words.
    """
    return [sentence.lower() for sentence in sentences if len(sentence) >= length]


def get_sentences_with_length_and_sentences_with_length_and_sentences_with_length(text, length, sentences):
    """
    Given a string, return a list of sentences, where each sentence is a list of words