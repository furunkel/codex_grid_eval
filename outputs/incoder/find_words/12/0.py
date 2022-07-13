
def find_char_long(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
    longwords = []
    for word in text.split():
        if len(word) >= 20:
            longwords.append(word)
    return longwords

def remove_long_words(text):
    """
    Removes all words which are at least 20 characters long in a string.
    """
    longwords = find_char_long(text)
    words = text.split()
    for word in longwords:
        words.remove(word)
    return ' '.join(words)

def remove_short_words(text):
    """
    Removes all words which are less than 5 characters long in a string.
    """
    shortwords = find_char_short(text)
    words = text.split()
    for word in shortwords:
        words.remove(word)
    return ' '.join(words)

def remove_stopwords(text):
    """
    Removes all stopwords from a string.
    """
    stopwords = nltk.corpus.stopwords.words('english')
    words = text.split()
    for word in words:
        if word not in stopwords:
            words.remove(word)
    return ' '.join(words)

def remove_non_ascii(text):
    """
    Removes all non-ascii characters from a string.
    """
    return text.encode('ascii', 'ignore').decode('ascii')

def remove_non_alphanumeric(text):
    """
    Removes all non-alphanumeric characters from a string.
    """
    return re.sub('\W+', ' ', text)

def remove_non_words(text):
    """
    Removes all non-words from a string.
    """
    words = text.split()
    for word in words:
        if word not in nltk.corpus.words.words():
            words.remove(word)
    return ' '.join(words)

def remove_non_alphanumeric_words(text):
    """
    Removes all non-alphanumeric words from a string.
    """
    words = text.split()
    for word in words:
        if word not in nltk.corpus.words.words():
            words.remove(word)
    return ' '.join(words)

def remove_non_alphanumeric_chars(text):
    """
    Removes all non-alphanumeric characters from a string.
    """
    words = text.split()
    for word in words:
        if word not in nltk.corpus.words.words():
            words.remove(word)
    return ' '.join(words)

def remove_non_alphanumeric_chars_and_spaces(text):
    """
    Removes all non-alphanumeric characters and spaces from a string.
    """
    words = text.split()
    for word in words:
        if word not in nltk.corpus.words.words():
            words.remove(word)
    return ' '.join(words)

def remove_non_alphanumeric_chars_and_spaces_words(text):
    """
    Removes all non-alphanumeric characters and spaces from a string.
    """
    words = text.split()
    for word in words:
        if word not in nltk.corpus.words.words():
            words.remove(word)
    return ' '.join(words)