
def string_to_hash(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def hash_to_string(hash_value):
    """
    Given a hash value 'hash_value', return its string equivalent.
    If 'hash_value' is an empty string, return None.
    """
    if hash_value == "":
        return None
    else:
        return hash_value.encode('utf-8')


def get_hash_value(text):
    """
    Given a string 'text', return its hash value.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return string_to_hash(text)


def get_string(hash_value):
    """
    Given a hash value 'hash_value', return its string equivalent.
    If 'hash_value' is an empty string, return None.
    """
    if hash_value == "":
        return None
    else:
        return hash_to_string(hash_value)


def get_hash_value_from_file(file_path):
    """
    Given a file path 'file_path', return its hash value.
    If 'file_path' is an empty string, return None.
    """
    if file_path == "":
        return None
    else:
        return string_to_hash(get_string_from_file(file_path))


def get_string_from_file(file_path):
    """
    Given a file path 'file_path', return its string equivalent.
    If 'file_path' is an empty string, return None.
    """
    if file_path == "":
        return None
    else:
        with open(file_path, 'r') as f:
            return f.read()


def get_hash_value_from_url(url):
    """
    Given a url 'url', return its hash value.
    If 'url' is an empty string, return None.
    """
    if url == "":
        return