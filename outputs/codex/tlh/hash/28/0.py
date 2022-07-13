
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA1 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    return hashlib.sha1(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(filename):
    """
    Ach batlh ghIlghameS 'filename' neH SHA1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('sha1.py') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def ghop_D_hash_file_chunks(filename, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH SHA1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('sha1.py') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            sha1.update(chunk)
    return sha1.hexdigest()


def ghop_D_hash_file_chunks_with_callback(filename, callback, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH SHA1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks_with_callback('sha1.py') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """