
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with six underscores and False otherwise.
    """
    return re.search(r'[A-Z]{2,}_+[A-Z]{2,}', text) is not None

def find_email_addresses(text):
    """
    Write a function that returns a list of all email addresses in a string.
    """
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)

def find_phone_numbers(text):
    """
    Write a function that returns a list of all phone numbers in a string.
    """
    return re.findall(r'\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}', text)

def find_urls(text):
    """
    Write a function that returns a list of all URLs in a string.
    """
    return re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)

def find_dates(text):
    """
    Write a function that returns a list of all dates in a string.
    """
    return re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', text)

def find_times(text):
    """
    Write a function that returns a list of all times in a string.
    """
    return re.findall(r'\d{1,2}:\d{2}(?::\d{2})?(?:[ap]m)?', text)

def find_money(text):
    """
    Write a function that returns a list of all monetary amounts in a string.
    """
    return re.findall(r'\$\d+(?:\.\d{2})?', text)

def find_zip_codes(text):
    """
    Write a function that returns a list of all zip codes in a string.
    """
    return re.findall(r'\d{5}(?:-\d{4})?', text)
