
def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA512 hash string, return its string equivalent (e.g.
    'da39a3ee5e6b4b0d3255bfef95601890afd80709').
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return hash[:32].decode('utf-8')


def hash_exists(hash, text):
    """
    Given a SHA512 hash string and a string 'text', return whether the
    string 'text' exists in the hash 'hash'.
    """
    return hash_to_string(hash) == text


def hash_matches(hash, text):
    """
    Given a SHA512 hash string and a string 'text', return whether the
    string 'text' matches the hash 'hash'.
    """
    return hash_exists(hash, text) and hash_to_string(hash) == text


def hash_matches(hash1, hash2, text):
    """
    Given two SHA512 hash strings and a text string, return whether the
    text string matches the hash 'hash1'.
    """
    return hash_exists(hash1, text) and hash_matches(hash2, text)


def hash_matches(hash1, hash2, text):
    """
    Given two SHA512 hash strings and a text string, return whether the
    text string matches the hash 'hash1'.
    """
    return hash_exists(hash1, text) and hash_matches(hash2, text)


def hash_matches(hash1, hash2, text):
    """
    Given two SHA512 hash strings and a text string, return whether the
    text string matches the hash 'hash1'.
    """
    return hash_exists(hash1, text) and hash_matches(hash2, text)


def hash_matches(hash1, hash2, text):
    """
    Given two SHA512 hash strings and a text string, return whether the
    text string matches the hash 'hash1'.
    """
    return hash_exists(hash1, text) and hash_matches(hash2, text)


def hash_matches(hash1, hash2, text):
    """
    Given two SHA512 hash strings and a text string, return whether the
    text string matches the hash 'hash1'.
    """
    return hash_exists(hash1, text) and hash_matches(hash2, text)


def hash_matches(hash1, hash2, text):
    """
    Given two SHA512 hash strings and a text string, return whether the
    text string matches the hash 'hash1'.
    """
    return hash_exists(hash1, text) and hash_matches(hash2, text)


def hash_matches(hash1, hash2, text):
    """
    Given two SHA512 hash strings and 