
def find_char_long(text):
    """
    Finds all words which are at least 3 characters long in a string.
    """
    return re.findall(r'\b\w{3,}\b', text)

def find_char_long_vowels(text):
    """
    Finds all words which are at least 3 characters long and contain at least 2 vowels in a string.
    """
    return re.findall(r'\b\w*[aeiou]{2,}\w*\b', text)

def find_char_long_vowels_consonants(text):
    """
    Finds all words which are at least 3 characters long and contain at least 2 vowels and 2 consonants in a string.
    """
    return re.findall(r'\b\w*[aeiou]{2,}\w*[bcdfghjklmnpqrstvwxyz]{2,}\w*\b', text)

def find_char_long_vowels_consonants_punctuation(text):
    """
    Finds all words which are at least 3 characters long and contain at least 2 vowels, 2 consonants and 1 punctuation in a string.
    """
    return re.findall(r'\b\w*[aeiou]{2,}\w*[bcdfghjklmnpqrstvwxyz]{2,}\w*[.,!?]\w*\b', text)

def find_char_long_vowels_consonants_punctuation_numbers(text):
    """
    Finds all words which are at least 3 characters long and contain at least 2 vowels, 2 consonants, 1 punctuation and 1 number in a string.
    """
    return re.findall(r'\b\w*[aeiou]{2,}\w*[bcdfghjklmnpqrstvwxyz]{2,}\w*[.,!?]\w*[0-9]\w*\b', text)

def find_char_long_vowels_consonants_punctuation_numbers_capitals(text):
    """
    Finds all words which are at least 3 characters long and contain at least 2 vowels