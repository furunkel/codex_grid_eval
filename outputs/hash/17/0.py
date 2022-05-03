
def string_to_hash(text):
    """
    Given a string 'text', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_hash_of_file(file_path):
    """
    Given a file path 'file_path', return its sha-512 hash equivalent string.
    If 'file_path' is an empty string, return None.

    >>> get_hash_of_file('test.txt') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if file_path == '':
        return None
    else:
        with open(file_path, 'rb') as f:
            return hashlib.sha512(f.read()).hexdigest()


def get_hash_of_directory(directory_path):
    """
    Given a directory path 'directory_path', return its sha-512 hash equivalent string.
    If 'directory_path' is an empty string, return None.

    >>> get_hash_of_directory('test_dir') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if directory_path == '':
        return None
    else:
        return hashlib.sha512(directory_path.encode('utf-8')).hexdigest()


def get_hash_of_directory_recursive(directory_path):
    """
    Given a directory path 'directory_path', return its sha-512 hash equivalent string.
    If 'directory_path' is an empty string, return None.

    >>> get_hash_of