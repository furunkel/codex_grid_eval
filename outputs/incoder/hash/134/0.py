
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_to_string(hash):
    """
    Given a BLAKE2S hash string 'hash', return its string equivalent.
    If 'hash' is None, return an empty string.

    >>> hash_to_string('0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c') == 'Hallo welt'
    """
    if hash is None:
        return ''
    return blake2s(hash.encode()).hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_of_file(filename):
    """
    Given a filename 'filename', return its BLAKE2S hash equivalent string.
    If 'filename' is None, return None.

    >>> hash_of_file('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if filename is None:
        return None
    with open(filename, 'rb') as f:
        return blake2s(f.read()).hexdigest()


def hash_of_file_contents(file_contents):
    """
    Given a string 'file_contents', return its BLAKE2S hash equivalent string.
    If 'file_contents' is an empty string, return None.

    >>> hash_of_file_contents('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if file_contents == '':
        return None
    return blake2s(file_contents.encode()).hexdigest()


def hash_of_file_contents_stream(file_contents):
    """
    Given a string 'file_contents', return its BLAKE2S hash equivalent string.
    If 'file_contents' is an empty string, return None.

    >>> hash_of_file_contents_stream('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf