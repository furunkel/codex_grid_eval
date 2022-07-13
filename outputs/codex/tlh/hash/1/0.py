
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    return hashlib.md5(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(file_path):
    """
    Ach batlh ghIlghameS 'file_path' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test.txt') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def ghop_D_hash_file_chunks(file_path, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'file_path' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('test.txt') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def ghop_D_hash_file_chunks_with_progress(file_path, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'file_path' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks_with_progress('test.txt') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    md5 = hashlib