
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == '1bc29b36f623ba82aaf6724fd3b16718'
    """
    return hashlib.md5(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(file_path):
    """
    Ach batlh ghIlghameS 'file_path' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('/etc/passwd') == 'd7b9c7f9b9b4c9f9d9d9d9d9d9d9d9d9'
    """
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def ghop_D_hash_file_chunks(file_path, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'file_path' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('/etc/passwd') == 'd7b9c7f9b9b4c9f9d9d9d9d9d9d9d9d9'
    """
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def ghop_D_hash_file_chunks_with_callback(file_path, chunk_size=1024, callback=None):
    """
    Ach batlh ghIlghameS 'file_path' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks_with_callback('/etc