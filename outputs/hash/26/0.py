
def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def get_hash_from_file(file_path):
    """
    Given a file path 'file_path', return its SHA1 hash equivalent string.
    If 'file_path' is an empty string, return None.

    >>> get_hash_from_file('test.txt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if file_path == '':
        return None
    else:
        with open(file_path, 'rb') as f:
            return hashlib.sha1(f.read()).hexdigest()


def get_hash_from_url(url):
    """
    Given a URL 'url', return its SHA1 hash equivalent string.
    If 'url' is an empty string, return None.

    >>> get_hash_from_url('https://www.google.com') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if url == '':
        return None
    else:
        return hashlib.sha1(urlopen(url).read()).hexdigest()


def get_hash_from_string(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> get_hash_from_string('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def get_hash_from_file_path(file_path):
    """
    Given a file path 'file_path', return its SHA1 hash equivalent string.
    If 'file_path' is an empty string, return None.

    >>> get_hash_from_file_path('test.txt