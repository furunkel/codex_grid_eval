def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 1 bit position.
    """
    return int(a[0] - b[0]) != int(a[1] - b[1])


def get_file_size(path):
    """
    Returns the size of the given file.
    """
    return os.path.getsize(path)


def get_file_md5(path):
    """
    Returns the md5 of the given file.
    """
    return hashlib.md5(open(path, 'rb').read()).hexdigest()


def get_file_size_mb(path):
    """
    Returns the size of the given file in MB.
    """
    return os.path.getsize(path) / (1024 * 1024)


def get_file_md5_mb(path):
    """
    Returns the md5 of the given file in MB.
    """
    return hashlib.md5(open(path, 'rb').read()).hexdigest()


def get_file_size_gb(path):
    """
    Returns the size of the given file in GB.
    """
    return os.path.getsize(path) / (1024 * 1024 * 1024)


def get_file_md5_gb(path):
    """
    Returns the md5 of the given file in GB.
    """
    return hashlib.md5(open(path, 'rb').read()).hexdigest()


def get_file_size_tb(path):
    """
    Returns the size of the given file in TB.
    """
    return os.path.getsize(path) / (1024 * 1024 * 1024 * 1024)


def get_file_md5_tb(path):
    """
    Returns the md5 of the given file in TB.
    """
    return hashlib.md5(open(path, 'rb').read()).hexdigest()


def get_file_size_tb(path):
    """
    Returns the size of the given file in TB.
    """
    return os.path.getsize(path) / (1024 * 1024 * 1024 * 1024)


def get_file_md5_tb(path):
    """
    Returns the md5 of the given file in TB.
    """
    return hashlib.md5(open(path, 'rb').read()).hexdigest()

