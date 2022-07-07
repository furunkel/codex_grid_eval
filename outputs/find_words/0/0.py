
def find_char_long(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return re.findall(r'\b\w{1,}\b', text)

def find_char_long_v2(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return re.findall(r'\w{1,}', text)

def find_char_long_v3(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return re.findall(r'\w+', text)

def find_char_long_v4(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return re.findall(r'\w*', text)

def find_char_long_v5(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return re.findall(r'\w?', text)

def find_char_long_v6(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return re.findall(r'\w{1}', text)

def find_char_long_v7(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return re.findall(r'\w{2}', text)

def find_char_long_v8(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return re.findall(r'\w{3}', text)

def find_char_long_v9(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return re.findall(r'\w{4}', text)

def find_char_long_v10(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return re.findall(r'\w{5}', text)