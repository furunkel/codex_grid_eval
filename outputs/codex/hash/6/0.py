
def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def get_hash_of_file(file_path):
    """
    Given a file path 'file_path', return its MD5 hash equivalent string.
    If 'file_path' is an empty string, return None.
    """
    if file_path == '':
        return None
    else:
        return hashlib.md5(open(file_path, 'rb').read()).hexdigest()


def get_hash_of_file_object(file_object):
    """
    Given a file object 'file_object', return its MD5 hash equivalent string.
    If 'file_object' is None, return None.
    """
    if file_object is None:
        return None
    else:
        return hashlib.md5(file_object.read()).hexdigest()


def get_hash_of_file_object_in_chunks(file_object, chunk_size=1024):
    """
    Given a file object 'file_object', return its MD5 hash equivalent string.
    If 'file_object' is None, return None.
    """
    if file_object is None:
        return None
    else:
        md5_hash = hashlib.md5()
        for chunk in iter(lambda: file_object.read(chunk_size), b''):
            md5_hash.update(chunk)
        return md5_hash.hexdigest()


def get_hash_of_file_in_chunks(file_path, chunk_size=1024):
    """
    Given a file path 'file_path', return its MD5 hash equivalent string.
    If 'file_path' is an empty string, return None.
    """
    if file_path == '':
        return None
    else:
        md5_hash = hashlib.md5()
        with open(file_path, 'rb') as file_object:
            for chunk in iter(lambda: file_object.read(chunk_size), b''):
               