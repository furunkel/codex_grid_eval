
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH MD5 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hallo welt') == '05b7f4cbafdb32436fe8928f41ed8f64'
    """
    return hashlib.md5(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(filename):
    """
    Ach batlh ghIlghameS 'filename' neH MD5 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test.txt') == '05b7f4cbafdb32436fe8928f41ed8f64'
    """
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def ghop_D_hash_file_chunks(filename, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH MD5 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('test.txt') == '05b7f4cbafdb32436fe8928f41ed8f64'
    """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def ghop_D_hash_file_chunks_with_callback(filename, callback, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH MD5 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks_with_callback('test.txt') == '05b7f4cbafdb32436fe8928f41ed8f64'
    """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for