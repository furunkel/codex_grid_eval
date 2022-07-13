
def string_to_hash(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text).hexdigest()


def get_hash_from_file(filename):
    """
    Given a file 'filename', return its md5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_hash_from_file('test.txt') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if filename == '':
        return None
    else:
        with open(filename, 'r') as f:
            return hashlib.md5(f.read()).hexdigest()


def get_hash_from_url(url):
    """
    Given a url 'url', return its md5 hash equivalent string.
    If 'url' is an empty string, return None.

    >>> get_hash_from_url('http://www.google.com') == '1a79a4d60de6718e8e5b326e338ae533'
    """
    if url == '':
        return None
    else:
        return hashlib.md5(urllib2.urlopen(url).read()).hexdigest()


def get_hash_from_file_url(file_url):
    """
    Given a file url 'file_url', return its md5 hash equivalent string.
    If 'file_url' is an empty string, return None.

    >>> get_hash_from_file_url('http://www.google.com') == '1a79a4d60de6718e8e5b326e338ae533'
    """
    if file_url == '':
        return None
    else:
        return hashlib.md5(urllib2.urlopen(file_url).read()).hexdigest()


def get_hash_from_string(string):
    """
    Given a string 'string', return its md5 hash equivalent string.
    If 'string' is an empty string, return None.

    >>> get_hash_from_string('0') == 'cfcd208495d565ef66e7dff