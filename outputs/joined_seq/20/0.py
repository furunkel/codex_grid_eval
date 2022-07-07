
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with a minus and False otherwise.
    """
    return re.search(r'[A-Z]{2,}-[A-Z]{2,}', text) is not None

def find_all_joined_sequences(text):
    """
    Write a function that returns a list of all sequences of uppercase letters joined with a minus.
    """
    return re.findall(r'[A-Z]{2,}-[A-Z]{2,}', text)

def find_all_joined_sequences_with_spaces(text):
    """
    Write a function that returns a list of all sequences of uppercase letters joined with a minus, allowing for spaces.
    """
    return re.findall(r'[A-Z]{2,}(?:-|\s)[A-Z]{2,}', text)

def find_all_joined_sequences_with_spaces_or_dashes(text):
    """
    Write a function that returns a list of all sequences of uppercase letters joined with a minus or a space.
    """
    return re.findall(r'[A-Z]{2,}(?:-|\s)[A-Z]{2,}', text)

def find_all_joined_sequences_with_spaces_or_dashes_or_underscores(text):
    """
    Write a function that returns a list of all sequences of uppercase letters joined with a minus, a space, or an underscore.
    """
    return re.findall(r'[A-Z]{2,}(?:-|\s|_)[A-Z]{2,}', text)

def find_all_joined_sequences_with_spaces_or_dashes_or_underscores_or_periods(text):
    """
    Write a function that returns a list of all sequences of uppercase letters joined with a minus, a space, an underscore, or a period.
    """
    return re.findall(r'[A-Z]{2,}(?:-|\s|_|\.)[A-Z]{2,}', text)

def find_all_