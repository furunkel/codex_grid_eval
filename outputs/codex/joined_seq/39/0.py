
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with a dash and True otherwise.
    """
    return re.search(r'[a-z]+-[a-z]+', text) is None

def email_check(text):
    """
    Write a function to check if the input string is an email address.
    """
    return re.search(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+', text) is not None

def phone_check(text):
    """
    Write a function to check if the input string is a phone number.
    """
    return re.search(r'\d{3}-\d{3}-\d{4}', text) is not None

def money_check(text):
    """
    Write a function to check if the input string is a dollar amount.
    """
    return re.search(r'\$\d+\.\d{2}', text) is not None

def zip_check(text):
    """
    Write a function to check if the input string is a zip code.
    """
    return re.search(r'\d{5}', text) is not None

def date_check(text):
    """
    Write a function to check if the input string is a date.
    """
    return re.search(r'\d{2}/\d{2}/\d{4}', text) is not None

def password_check(text):
    """
    Write a function to check if the input string is a password.
    """
    return re.search(r'[a-zA-Z0-9]{8,}', text) is not None

def strong_password_check(text):
    """
    Write a function to check if the input string is a strong password.
    """
    return re.search(r'[a-z]+[A-Z]+[0-9]+', text) is not None

def extract_pid(log_line):
    """
    Write a function to extract the pid from a log line.
    """
    regex = r"\[(\d+)\]"
    result = re.search