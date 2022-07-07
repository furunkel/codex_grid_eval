
def find_char_long(text):
    """
    Finds all words which are not 3 characters long in a string.
    """
    return re.findall(r'\b\w{1,2}\b', text)

def find_char_short(text):
    """
    Finds all words which are not 3 characters long in a string.
    """
    return re.findall(r'\b\w{4,}\b', text)

def find_char_long_short(text):
    """
    Finds all words which are not 3 characters long in a string.
    """
    return re.findall(r'\b\w{1,2}\b|\b\w{4,}\b', text)

def find_char_long_short_v2(text):
    """
    Finds all words which are not 3 characters long in a string.
    """
    return re.findall(r'\b\w{1,2}|\w{4,}\b', text)

def find_char_long_short_v3(text):
    """
    Finds all words which are not 3 characters long in a string.
    """
    return re.findall(r'\b\w{1,2}|\w{4,}\b', text)

def find_char_long_short_v4(text):
    """
    Finds all words which are not 3 characters long in a string.
    """
    return re.findall(r'\b\w{1,2}|\w{4,}\b', text)

def find_char_long_short_v5(text):
    """
    Finds all words which are not 3 characters long in a string.
    """
    return re.findall(r'\b\w{1,2}|\w{4,}\b', text)

def find_char_long_short_v6(text):
    """
    Finds all words which are not 3 characters long in a string.
    """
    return re.findall(r'\b\w{1,2}|\w{4,}\b', text)

def find_char_long_short_v7(text):
    """
    Finds all words which