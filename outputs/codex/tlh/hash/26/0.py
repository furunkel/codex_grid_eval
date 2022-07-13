
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH SHA1 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    return hashlib.sha1(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(filename):
    """
    Ach batlh ghIlghameS 'filename' neH SHA1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test.txt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def ghop_D_hash_file_chunks(filename, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH SHA1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('test.txt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            sha1.update(chunk)
    return sha1.hexdigest()


def ghop_D_hash_file_chunks_mmap(filename, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH SHA1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks_mmap('test.txt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    sha1 = hashlib.sha1()
