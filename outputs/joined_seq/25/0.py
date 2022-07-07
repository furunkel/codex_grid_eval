
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with a dash and False otherwise.
    """
    return re.search(r'[a-z]+-[a-z]+', text)

def email_check(text):
    """
    Write a function to that returns True if the input string is a valid email address and False otherwise.
    """
    return re.search(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+', text)

def time_check(text):
    """
    Write a function to that returns True if the input string is a valid time in the format HH:MM (with 0 <= HH <= 23 and 0 <= MM <= 59) and False otherwise.
    """
    return re.search(r'[0-2][0-9]:[0-5][0-9]', text)

def phone_check(text):
    """
    Write a function to that returns True if the input string is a valid phone number (matching the format XXX-XXX-XXXX where X is a digit) and False otherwise.
    """
    return re.search(r'[0-9]{3}-[0-9]{3}-[0-9]{4}', text)

def money_check(text):
    """
    Write a function to that returns True if the input string is a valid monetary amount in the format $XXX.XX (with exactly two decimal places) and False otherwise.
    """
    return re.search(r'\$[0-9]{3}\.[0-9]{2}', text)

def zip_check(text):
    """
    Write a function to that returns True if the input string is a valid US zip code (matching the format XXXXX or XXXXX-XXXX where X is a digit) and False otherwise.
    """
    return re.search(r'[0-9]{5}(-[0-9]{4})?', text)

def date_check(text):
    """
    Write a function to that returns True if the input string is a valid date in the format MM/DD/YYYY (with 1 <= MM <= 12 and 1 <= DD <= 31) and False otherwise.
    """
    return re.