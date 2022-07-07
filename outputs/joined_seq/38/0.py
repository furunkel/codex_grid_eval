
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with a dash and True otherwise.
    """
    return re.search(r'[A-Z]{2,}-[A-Z]{2,}', text) is None

def email_check(text):
    """
    Write a function to check if the input string is an email address.
    """
    return re.search(r'[\w.-]+@[\w.-]+', text) is not None

def time_check(text):
    """
    Write a function to check for the time format of 'HH:MM' for the input string and return True if valid and False otherwise.
    """
    return re.search(r'^[0-2][0-9]:[0-5][0-9]$', text) is not None

def phone_check(text):
    """
    Write a function to check if the input string is a valid phone number.
    """
    return re.search(r'^\d{3}-\d{3}-\d{4}$', text) is not None

def money_check(text):
    """
    Write a function to check for a valid money amount of the format $123,456,789.00 and return True if valid and False otherwise.
    """
    return re.search(r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$', text) is not None

def zip_check(text):
    """
    Write a function to check if the input string is a valid zipcode
    """
    return re.search(r'^\d{5}(-\d{4})?$', text) is not None

def date_check(text):
    """
    Write a function to check if the input string is a valid date of the format YYYY-MM-DD.
    """
    return re.search(r'^\d{4}-\d{2}-\d{2}$', text) is not None

def password_check(text):
    """
    Write a function to check for a valid password.
    """
    return re.search(r'^(?=.*[a-z])(?=.*[A-