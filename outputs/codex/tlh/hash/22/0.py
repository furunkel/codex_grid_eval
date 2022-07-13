
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha1 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    return hashlib.sha1(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(file_path):
    """
    Ach batlh ghIlghameS 'file_path' neH sha1 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('/tmp/test.txt') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    with open(file_path, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def ghop_D_hash_file_chunks(file_path, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'file_path' neH sha1 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('/tmp/test.txt') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()


def ghop_D_hash_file_chunks_mmap(file_path, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'file_path' neH sha1 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks_mmap('/tmp/test.txt') == '415ab