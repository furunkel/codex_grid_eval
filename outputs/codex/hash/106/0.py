
def string_to_hash(text):
    """
    Given a string 'text', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('sha1', 'salt') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('sha1', 'salt', 1) == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha512((text + salt).encode('utf-8')).hexdigest()
        return text


def string_to_hash_with_salt_and_iterations_and_length(