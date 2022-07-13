
def find_char_long(text):
    """
    Finds all words which are at least 6 characters long in a string.
    """
    return re.findall(r'\b\w{6,}\b', text)

def find_char_long_vowel(text):
    """
    Finds all words which are at least 6 characters long and contain at least
    one vowel in a string.
    """
    return re.findall(r'\b\w*[aeiou]\w{5,}\b', text)

def find_char_long_vowel_consonant(text):
    """
    Finds all words which are at least 6 characters long and contain at least
    one vowel and one consonant in a string.
    """
    return re.findall(r'\b\w*[aeiou]\w*[^aeiou]\w{4,}\b', text)

def find_char_long_vowel_consonant_end(text):
    """
    Finds all words which are at least 6 characters long and contain at least
    one vowel and one consonant and end with a consonant in a string.
    """
    return re.findall(r'\b\w*[aeiou]\w*[^aeiou]\w*[^aeiou]\b', text)

def find_char_long_vowel_consonant_end_start(text):
    """
    Finds all words which are at least 6 characters long and contain at least
    one vowel and one consonant and end with a consonant and start with a
    consonant in a string.
    """
    return re.findall(r'\b[^aeiou]\w*[aeiou]\w*[^aeiou]\w*[^aeiou]\b', text)

def find_char_long_vowel_consonant_end_start_vowel(text):
    """
    Finds all words which are at least 6 characters long and contain at least
    one vowel and one consonant and end with a consonant and start with a
    consonant and contain at least one vowel in a string.
    """
    return re.findall(r'\b[