
def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def get_hash_from_file(file_path):
    """
    Given a file path, return its sha1 hash equivalent string.
    If the file does not exist, return None.
    """
    if not os.path.exists(file_path):
        return None
    else:
        with open(file_path, 'rb') as f:
            return hashlib.sha1(f.read()).hexdigest()


def get_hash_from_url(url):
    """
    Given a url, return its sha1 hash equivalent string.
    If the url does not exist, return None.
    """
    try:
        response = requests.get(url)
        return hashlib.sha1(response.content).hexdigest()
    except requests.exceptions.RequestException:
        return None


def get_hash_from_string(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def get_hash_from_file_or_url(file_or_url):
    """
    Given a file path or url, return its sha1 hash equivalent string.
    If the file or url does not exist, return None.
    """
    if os.path.exists(file_or_url):
        return get_hash_from_file(file_or_url)
    else:
        return get_hash_from_url(file_or_url)


def get_hash_from_file_or_string(file_or_string):
    """
    Given a file path or string, return its sha1 hash equivalent string.
    If the file or string does not exist, return None.
    """
    if os.path.exists(file_or_string):
