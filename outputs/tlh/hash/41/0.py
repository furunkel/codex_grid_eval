
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    return hashlib.sha224(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(file_path):
    """
    Ach batlh ghIlghameS 'file_path' neH sha224 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('/etc/passwd') == 'f8c8f8e8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8'
    """
    with open(file_path, 'rb') as f:
        return hashlib.sha224(f.read()).hexdigest()


def ghop_D_hash_file_chunks(file_path, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'file_path' neH sha224 hash ghopDu.
    qaSbe'chugh, vaj 'file_path' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('/etc/passwd') == 'f8c8f8e8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8'
    """
    with open(file_path, 'rb') as f:
        m = hashlib.sha224()
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            m.update(chunk)
        return m.hexdigest()


def ghop_D_hash_file_chunks_threaded(file_path, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'file_path' neH sha224 hash ghopDu.
    qaSbe'