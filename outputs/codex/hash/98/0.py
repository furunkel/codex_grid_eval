
def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return the SHA512 hash
    equivalent string of 'text' concatenated with 'salt'.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt('Hallo welt', 'salt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512((text + salt).encode('utf-8')).hexdigest()


def string_to_hash_with_salt_and_iterations(text, salt, iterations):
    """
    Given a string 'text', a string 'salt', and an integer 'iterations',
    return the SHA512 hash equivalent string of 'text' concatenated with
    'salt' and hashed 'iterations' times.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_salt_and_iterations('Hallo welt', 'salt', 1) == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if text == '':
        return None
    else:
        for i in range(iterations):
            text = hashlib.sha512((text + salt).encode('utf