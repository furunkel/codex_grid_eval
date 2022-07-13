
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    return hashlib.sha224(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(filename):
    """
    Ach batlh ghIlghameS 'filename' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test.txt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha224(f.read()).hexdigest()


def ghop_D_hash_file_chunks(filename, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('test.txt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    h = hashlib.sha224()
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def ghop_D_hash_file_chunks_mmap(filename, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks_mmap('test.txt') == 'fa69fc6cbf7cb57890a921eae