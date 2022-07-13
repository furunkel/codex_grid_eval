
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with a minus and False otherwise.
    """

def get_words(text):
    """
    Return a list of lowercase words in the given text.
    """
    return [word.lower() for word in text.split()]

def get_sentences(text):
    """
    Return a list of sentences in the given text.
    """
    return [sentence.strip() for sentence in text.split('\n')]

def get_sentences_with_length(text, length):
    """
    Return a list of sentences in the given text, where each sentence is a list of words.
    """
    return [sentence.strip() for sentence in text.split('\n') if len(sentence) >= length]

def get_sentences_with_length_and_sentences(text, length, sentences):
    """
    Return a list of sentences in the given text, where each sentence is a list of words.
    """
    return [sentence.strip() for sentence in sentences if len(sentence) >= length]

def get_sentences_with_length_and_sentences_with_length(text, length, sentences):
    """
    Return a list of sentences in the given text, where each sentence is a list of words.
    """
    return [sentence.strip() for sentence in sentences if len(sentence) >= length]

def get_sentences_with_length_and_sentences_with_length_and_sentences(text, length, sentences):
    """
    Return a list of sentences in the given text, where each sentence is a list of words.
    """
    return [sentence.strip() for sentence in sentences if len(sentence) >= length]

def get_sentences_with_length_and_sentences_with_length_and_sentences_with_length_and_sentences(text, length, sentences):
    """
    Return a list of sentences in the given text, where each sentence is a list of words.
    """
    return [sentence.strip() for sentence in sentences if len(sentence) >= length]

def get_sentences_with_length_and_sentences_with_length_and_sentences_with_length_and_sentences_with_length_and_sentences(text, length, sentences):
    """
    Return