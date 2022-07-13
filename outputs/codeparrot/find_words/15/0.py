
def find_char_long(text):
    """
    Finds all words which are not 20 characters long in a string.
    """
#    print "find_char_long: text = %s" % text
    if len(text) < 20:
        return []
    else:
        return [x for x in text if len(x) > 20]

def find_char_short(text):
    """
    Finds all words which are not 20 characters short in a string.
    """
#    print "find_char_short: text = %s" % text
    if len(text) < 20:
        return []
    else:
        return [x for x in text if len(x) < 20]

def find_char_long_short(text):
    """
    Finds all words which are not 20 characters long in a string.
    """
#    print "find_char_long_short: text = %s" % text
    if len(text) < 20:
        return []
    else:
        return [x for x in text if len(x) > 20]

def find_char_short_long(text):
    """
    Finds all words which are not 20 characters short in a string.
    """
#    print "find_char_short_long: text = %s" % text
    if len(text) < 20:
        return []
    else:
        return [x for x in text if len(x) > 20]

def find_char_long_long(text):
    """
    Finds all words which are not 20 characters long in a string.
    """
#    print "find_char_long_long: text = %s" % text
    if len(text) < 20:
        return []
    else:
        return [x for x in text if len(x) > 20]

def find_char_short_short(text):
    """
    Finds all words which are not 20 characters short in a string.
    """
#    print "find_char_short_short: text = %s" % text
    if len(text) < 20:
        return []
    else:
        return [x for x in text if len(x) > 20]

def find_char_long_short_long(text):
    """
    Finds all words which are not 20 characters long in a