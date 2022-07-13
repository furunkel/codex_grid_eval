
def find_char_long(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
#    print "find_char_long: text = %s" % text
    if len(text) < 20:
        return []
    return [x for x in text.split() if len(x) >= 20]

def find_char_short(text):
    """
    Finds all words which are at least 20 characters short in a string.
    """
#    print "find_char_short: text = %s" % text
    if len(text) < 20:
        return []
    return [x for x in text.split() if len(x) <= 20]

def find_char_space(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
#    print "find_char_space: text = %s" % text
    if len(text) < 20:
        return []
    return [x for x in text.split() if len(x) >= 20]

def find_char_not_space(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
#    print "find_char_not_space: text = %s" % text
    if len(text) < 20:
        return []
    return [x for x in text.split() if len(x) >= 20]

def find_char_not_word(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
#    print "find_char_not_word: text = %s" % text
    if len(text) < 20:
        return []
    return [x for x in text.split() if len(x) >= 20]

def find_char_not_word_or_space(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
#    print "find_char_not_word_or_space: text = %s" % text
    if len(text) < 20:
        return []
    return [x for x in text.split() if len(x) >= 20]

def find_char_not_word_or_space_or_not_