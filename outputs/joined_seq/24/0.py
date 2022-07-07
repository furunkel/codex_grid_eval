
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with a dash and False otherwise.
    """
    return re.search(r'[A-Z]{2,}-[A-Z]{2,}', text)

def email_check(text):
    """
    Write a function to check if the input string is an email address.
    """
    return re.search(r'[\w.-]+@[\w.-]+', text)

def time_check(text):
    """
    Write a function to check if the input string is a valid time.
    """
    return re.search(r'^[0-9]{1,2}:[0-9]{2}$', text)

def phone_check(text):
    """
    Write a function to check if the input string is a valid phone number.
    """
    return re.search(r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$', text)

def money_check(text):
    """
    Write a function to check if the input string is a valid dollar amount.
    """
    return re.search(r'^\$[0-9]+(\.[0-9]{2})?$', text)

def zip_check(text):
    """
    Write a function to check if the input string is a valid zip code.
    """
    return re.search(r'^[0-9]{5}(?:-[0-9]{4})?$', text)

def date_check(text):
    """
    Write a function to check if the input string is a valid date.
    """
    return re.search(r'^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$', text)

def hex_check(text):
    """
    Write a function to check if the input string is a valid hex code.
    """
    return re.search(r'^#[0-9a-fA-F]{6}$', text)

def strong_password_check(text):
    """
    Write a function to check if the input string is a strong password