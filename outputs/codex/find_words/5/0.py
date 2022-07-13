
def find_char_long(text):
    """
    Finds all words which are exactly 3 characters long in a string.
    """
    return re.findall(r'\b\w{3}\b', text)

def find_char_long_or_short(text):
    """
    Finds all words which are exactly 3 characters long or exactly 4 characters long in a string.
    """
    return re.findall(r'\b\w{3,4}\b', text)

def find_char_long_and_short(text):
    """
    Finds all words which are exactly 3 characters long and exactly 4 characters long in a string.
    """
    return re.findall(r'\b\w{3}\b\s\b\w{4}\b', text)

def find_char_long_or_short_or_long(text):
    """
    Finds all words which are exactly 3 characters long or exactly 4 characters long or exactly 5 characters long in a string.
    """
    return re.findall(r'\b\w{3,5}\b', text)

def find_char_long_and_short_and_long(text):
    """
    Finds all words which are exactly 3 characters long and exactly 4 characters long and exactly 5 characters long in a string.
    """
    return re.findall(r'\b\w{3}\b\s\b\w{4}\b\s\b\w{5}\b', text)

def find_char_long_or_short_or_long_or_short(text):
    """
    Finds all words which are exactly 3 characters long or exactly 4 characters long or exactly 5 characters long or exactly 6 characters long in a string.
    """
    return re.findall(r'\b\w{3,6}\b', text)

def find_char_long_and_short_and_long_and_short(text):
    """
    Finds all words which are exactly 3 characters long and exactly 4 characters long and exactly 5 characters long and exactly 6 characters long in a string.
    """
    return re.findall(r'\b\w{3}\b\s\b\w{4}\b\s\b\w{5}\b\s\b\w