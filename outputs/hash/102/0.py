
def string_to_hash(text):
    """
    Given a string 'text', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return hashlib.sha512(text.encode()).hexdigest()


def hash_to_string(hash_string):
    """
    Given a hash string 'hash_string', return its string equivalent.
    If 'hash_string' is an empty string, return None.
    """
    if hash_string == "":
        return None
    else:
        return hash_string.encode().decode()


def get_hash_value(hash_string):
    """
    Given a hash string 'hash_string', return its integer value.
    If 'hash_string' is an empty string, return None.
    """
    if hash_string == "":
        return None
    else:
        return int(hash_string, 16)


def get_hash_bucket(hash_value, bucket_size):
    """
    Given a hash value 'hash_value' and a bucket size 'bucket_size',
    return the bucket number as a string.
    """
    return str(hash_value % bucket_size)


def get_hash_range_start(hash_value, bucket_size):
    """
    Given a hash value 'hash_value' and a bucket size 'bucket_size',
    return the start of the range as a string.
    """
    return str(hash_value - (hash_value % bucket_size))


def get_hash_range_end(hash_value, bucket_size):
    """
    Given a hash value 'hash_value' and a bucket size 'bucket_size',
    return the end of the range as a string.
    """
    return str((hash_value - (hash_value % bucket_size)) + bucket_size - 1)


def get_hash_range(hash_value, bucket_size):
    """
    Given a hash value 'hash_value' and a bucket size 'bucket_size',
    return the range as a string.
    """
    return get_hash_range_start(hash_value, bucket_size) + "-" + get_hash_range_end(hash_value, bucket_size