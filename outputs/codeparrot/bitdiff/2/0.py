def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly one bit position.
    """
    return int(a[0] - b[0]) != int(a[1] - b[1])


def get_all_files(directory):
    """
    Returns all files in a directory.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)]


def get_all_files_in_directory(directory):
    """
    Returns all files in a directory.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)]


def get_all_files_in_directory_with_extension(directory, extension):
    """
    Returns all files in a directory with a specific extension.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.endswith(extension)]


def get_all_files_in_directory_with_extension_and_extension(directory, extension):
    """
    Returns all files in a directory with a specific extension and extension.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.endswith(extension) and f.startswith(extension)]


def get_all_files_in_directory_with_extension_and_extension_and_extension_and_extension(directory, extension, extension_to_find):
    """
    Returns all files in a directory with a specific extension and extension.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.endswith(extension) and f.startswith(extension_to_find)]


def get_all_files_in_directory_with_extension_and_extension_and_extension_and_extension_and_extension_and_extension(directory, extension, extension_to_find, extension_to_find_in_directory):
    """
    Returns all files in a directory with a specific extension and extension.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.endswith(extension) and f.startswith(extension_to_find_in_directory)]


