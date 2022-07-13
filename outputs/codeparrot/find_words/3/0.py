
def find_char_long(text):
    """
    Finds all words which are not 1 characters long in a string.
    """
#    print "find_char_long: text = %s" % text
    if len(text) < 1:
        return []
    else:
        return [i for i in range(len(text)) if text[i] != ""]

def find_char_short(text):
    """
    Finds all words which are not 1 characters short in a string.
    """
#    print "find_char_short: text = %s" % text
    if len(text) < 1:
        return []
    else:
        return [i for i in range(len(text)) if text[i] != ""]

def find_char_long_short(text):
    """
    Finds all words which are not 1 characters long in a string.
    """
#    print "find_char_long_short: text = %s" % text
    if len(text) < 1:
        return []
    else:
        return [i for i in range(len(text)) if text[i] != ""]

def find_char_short_long(text):
    """
    Finds all words which are not 1 characters long in a string.
    """
#    print "find_char_short_long: text = %s" % text
    if len(text) < 1:
        return []
    else:
        return [i for i in range(len(text)) if text[i] != ""]

def find_char_long_long(text):
    """
    Finds all words which are not 1 characters long in a string.
    """
#    print "find_char_long_long: text = %s" % text
    if len(text) < 1:
        return []
    else:
        return [i for i in range(len(text)) if text[i] != ""]

def find_char_short_short(text):
    """
    Finds all words which are not 1 characters short in a string.
    """
#    print "find_char_short_short: text = %s" % text
    if len(text) < 1:
        return []
    else:
        return [i for i in range(len(text)) if text[i] != "