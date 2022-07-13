
def string_to_hash(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    return sha512(text).hexdigest()


def hash_to_string(hash):
    """
    Given a sha512 hash string, return its string equivalent hash.
    If 'hash' is an empty string, return None.
    """
    if hash == "":
        return None
    return sha512(hash).hexdigest()


def hash_exists(hash, text):
    """
    Given a sha512 hash string and a string 'text', return True if the
    hash is equal to the given hash and False otherwise.
    """
    return hash_to_string(hash) == text


def hash_not_exists(hash, text):
    """
    Given a sha512 hash string and a string 'text', return True if the
    hash is not equal to the given hash and False otherwise.
    """
    return hash_to_string(hash) != text


def hash_matches(hash, text):
    """
    Given a sha512 hash string and a string 'text', return True if the
    hash matches the given hash and False otherwise.
    """
    return hash_exists(hash, text) and hash_not_exists(hash, text)


def hash_not_matches(hash, text):
    """
    Given a sha512 hash string and a string 'text', return True if the
    hash does not match the given hash and False otherwise.
    """
    return hash_not_exists(hash, text) and hash_exists(hash, text)


def hash_not_in_set(hash, text, set_):
    """
    Given a sha512 hash string and a string 'text', return True if the
    hash does not appear in the given set and False otherwise.
    """
    return hash_not_exists(hash, text) and hash_exists(hash, text) not in set_


def hash_not_in_set_or(hash, text, set_):
    """
    Given a sha512 hash string and a string 'text', return True if the
    hash does not appear in the given set or False otherwise.
    """
    return hash_not_exists(hash, text) or hash_exists(hash, text) not in set_


def hash_not_in_set_and(hash, text, set_):
    """
    Given a sha512 hash string and a string 'text', return True if the
    hash does not appear in the given set and False otherwise.
    """
    return hash_not_exists(hash, text) and hash_exists(hash, text) not in set_


def hash_not_in_set_ornot(hash, text, set_):
    """
    Given a sha512 hash string and a string 'text', return True if the
    hash does not appear in the given set or False otherwise.
    """
    return hash_not_exists(hash, text) or hash_exists(hash, text) not in set_


def hash_not_in_set_andnot(hash, text, set_):
    """
    Given a sha512 hash string and a string 'text', return True if the
    hash does not appear in the given 