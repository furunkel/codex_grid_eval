def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with a question mark and False otherwise.
    """
    return text.lower() in string.lowercase


def split_into_sentences(text):
    """
    Splits a string into sentences.
    """
    return text.split()


def split_into_sentences_with_punctuation(text):
    """
    Splits a string into sentences, punctuation and punctuation.
    """
    return text.split(punctuation)


def split_into_sentences_with_numbers(text):
    """
    Splits a string into sentences, numbers and punctuation.
    """
    return text.split(numbers)


def split_into_sentences_with_punctuation_and_numbers(text):
    """
    Splits a string into sentences, punctuation and punctuation and numbers.
    """
    return text.split(punctuation) + text.split(numbers)


def split_into_sentences_with_numbers_and_punctuation(text):
    """
    Splits a string into sentences, numbers and punctuation and numbers and punctuation.
    """
    return split_into_sentences_with_punctuation_and_numbers(text) + split_into_sentences_with_numbers_and_punctuation(text)


def split_into_sentences_with_punctuation_and_numbers_and_punctuation(text):
    """
    Splits a string into sentences, punctuation and numbers and punctuation and numbers and punctuation.
    """
    return split_into_sentences_with_punctuation_and_numbers(text) + split_into_sentences_with_numbers_and_punctuation(text)


def split_into_sentences_with_numbers_and_punctuation_and_numbers(text):
    """
    Splits a string into sentences, numbers and punctuation and numbers and punctuation and numbers and punctuation.
    """
    return split_into_sentences_with_punctuation_and_numbers(text) + split_into_sentences_with_numbers_and_punctuation(text)


def split_into_sentences_with_punctuation_and_numbers_and_punctuation(text):
    """
    Splits a string into sentences, punctuation and numbers and punctuation and numbers and punctuation.
    """
    return split_into_sentences_with_punctuation_and_numbers(text) + split_into_sentences_