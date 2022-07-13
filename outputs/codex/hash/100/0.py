
def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA512 hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9') == 'sha1'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha512(hash.encode('utf-8')).hexdigest()


def hash_to_int(hash):
    """
    Given a SHA512 hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9') == 5
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its SHA512 hash equivalent.
    If 'integer' is 0, return None.

    >>> int_to_hash(5) == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6