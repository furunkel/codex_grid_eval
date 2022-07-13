
def string_to_hash(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if text == '':
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99') == '0'
    """
    if hash == '':
        return None
    for i in range(len(hash)):
        text = hash_to_string_helper(hash, i)
        if text:
            return text


def hash_to_string_helper(hash, i):
    """
    Given a hash 'hash' and an integer 'i', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string_helper('31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99', 0) == '0'
    """
    if hash == '':
        return None
    elif len(hash) < 128:
        return None
    else:
        text = str(i)
        return verify_hash(text, hash)


def verify_hash(text, hash):
    """
    Given a string 'text' and a hash 'hash', return the string 'text' if the hash of 'text' is equal to 'hash'.
    If 'text' is an empty string, return None.
    If 'hash' is an empty string, return None.

    >>> verify_hash('0', '31bca02094eb78126a517b