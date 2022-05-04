
def string_to_hash(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb') == 'Hallo welt'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha512(hash.encode('utf-8')).hexdigest()


def hash_equal(hash1, hash2):
    """
    Given two hashes 'hash1' and 'hash2', return True if they are equal, False otherwise.
    If 'hash1' or 'hash2' is an empty string, return None.

    >>> hash_equal('9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb', '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb')
    """
    if hash1 == '' or hash2 == '':
        return None
    else:
        return hash1 == hash2


def hash_index(keyword, buckets):
    """
    Given a keyword and the number of buckets, return the bucket where it belongs.