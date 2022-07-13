
def find_char_long(text):
    """
    Finds all words which are at least 6 characters long in a string.
    """
#    print "find_char_long", text
    if len(text) < 6:
        return []
    return [i for i in range(0, len(text)) if text[i] == " " * 6]

def find_char_short(text):
    """
    Finds all words which are at least 6 characters short in a string.
    """
#    print "find_char_short", text
    if len(text) < 6:
        return []
    return [i for i in range(0, len(text)) if text[i] == " " * 6]

def find_char_space(text):
    """
    Finds all words which are at least 6 characters long in a string.
    """
#    print "find_char_space", text
    if len(text) < 6:
        return []
    return [i for i in range(0, len(text)) if text[i] == " " * 6]

def find_char_not_space(text):
    """
    Finds all words which are at least 6 characters long in a string.
    """
#    print "find_char_not_space", text
    if len(text) < 6:
        return []
    return [i for i in range(0, len(text)) if text[i] != " " * 6]

def find_char_not_word(text):
    """
    Finds all words which are at least 6 characters long in a string.
    """
#    print "find_char_not_word", text
    if len(text) < 6:
        return []
    return [i for i in range(0, len(text)) if text[i] != " " * 6]

def find_char_not_word_or_space(text):
    """
    Finds all words which are at least 6 characters long in a string.
    """
#    print "find_char_not_word_or_space", text
    if len(text) < 6:
        return []
    return [i for i in range(0, len(text)) if text[i] != " " * 6]

def find_char_not_word_or_