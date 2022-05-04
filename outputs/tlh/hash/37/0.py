
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    return hashlib.sha224(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_file(filename):
    """
    Ach batlh ghIlghameS 'filename' neH sha224 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test.txt') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha224(f.read()).hexdigest()

def ghop_D_hash_file_chunks(filename, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH sha224 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('test.txt') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    h = hashlib.sha224()
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def ghop_D_hash_file_chunks_threaded(filename, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH sha224 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks_threaded('test.txt') == 'ac230f15fcae7f77d8f76e99adf45864a