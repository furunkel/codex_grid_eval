
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with a minus and True otherwise.
    """
    return re.search(r'[A-Z]{2,}-[A-Z]{2,}', text) is None

def is_valid_email(email):
    """
    Write a function to check if the input string is a valid email address.
    """
    return re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None

def is_valid_phone_number(phone):
    """
    Write a function to check if the input string is a valid phone number.
    """
    return re.search(r'^\d{3}-\d{3}-\d{4}$', phone) is not None

def is_valid_date(date):
    """
    Write a function to check if the input string is a valid date.
    """
    return re.search(r'^\d{2}/\d{2}/\d{4}$', date) is not None

def is_valid_credit_card(card):
    """
    Write a function to check if the input string is a valid credit card number.
    """
    return re.search(r'^\d{4}-\d{4}-\d{4}-\d{4}$', card) is not None

def is_valid_zip_code(zip_code):
    """
    Write a function to check if the input string is a valid zip code.
    """
    return re.search(r'^\d{5}$', zip_code) is not None

def is_valid_ip_address(ip):
    """
    Write a function to check if the input string is a valid IP address.
    """
    return re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip) is not None

def is_valid_url(url):
    """
    Write a function to check if the input string is a valid