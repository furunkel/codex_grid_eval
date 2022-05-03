
def string_to_hash(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_hash_from_file(filename):
    """
    Given a file 'filename', return its sha512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_hash_from_file('test.txt') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if filename == '':
        return None
    else:
        with open(filename, 'rb') as f:
            return hashlib.sha512(f.read()).hexdigest()


def get_hash_from_url(url):
    """
    Given a url 'url', return its sha512 hash equivalent string.
    If 'url' is an empty string, return None.

    >>> get_hash_from_url('https://www.google.com') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if url == '':
        return None
    else:
        return hashlib.sha512(requests.get(url).content).hexdigest()


def get_hash_from_file_url(file_url):
    """
    Given a file url 'file_url', return its sha512 hash equivalent string.
    If 'file_url' is an empty string, return None.

    >>> get_hash_from_file_url('https://www.google.com') == 'b7f783baed8297