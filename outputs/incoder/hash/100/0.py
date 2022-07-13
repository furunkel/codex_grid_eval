
def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if text == '':
        return None
    return sha512(text).hexdigest()


def hash_of_file(filename):
    """
    Given a filename 'filename', return the SHA512 hash equivalent string
    of the contents of the file 'filename'.  If 'filename' is an empty
    string, return None.

    >>> hash_of_file('sha512_of_this_file.txt') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        return sha512(f.read()).hexdigest()


def hash_of_directory(directory):
    """
    Given a directory 'directory', return the SHA512 hash equivalent string
    of the contents of the directory 'directory'.  If 'directory' is an empty
    string, return None.

    >>> hash_of_directory('sha512_of_this_directory') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if directory == '':
        return None
    return sha512(os.listdir(directory)).hexdigest()


def hash_of_directory_tree(directory):
    """
    Given a directory 'directory', return the SHA512 hash equivalent string
    of the contents of the directory 'directory'.  If 'directory' is an empty
    string, return None.

    >>> hash_of_directory_tree('sha512_of_this_directory') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if directory == '':
        return None
    return sha512(os.listdir(directory)).hexdigest()


def hash_of_directory_tree_with_contents(directory):
    """
    Given a directory 'directory', return the SHA512 hash equivalent string
    of the contents of the directory 'directory'.  If 'directory' is an empty
    string, return None.

    >>> hash_