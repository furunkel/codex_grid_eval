
def string_to_hash(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if text == '':
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_hash_from_file(file_path):
    """
    Given a file path 'file_path', return its sha512 hash equivalent string.
    If 'file_path' is an empty string, return None.

    >>> get_hash_from_file('test.txt') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if file_path == '':
        return None
    with open(file_path, 'rb') as f:
        return hashlib.sha512(f.read()).hexdigest()


def get_hash_from_url(url):
    """
    Given a url 'url', return its sha512 hash equivalent string.
    If 'url' is an empty string, return None.

    >>> get_hash_from_url('https://www.google.com') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    if url == '':
        return None
    return hashlib.sha512(requests.get(url).content).hexdigest()


def get_hash_from_string(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> get_hash_from_string('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c