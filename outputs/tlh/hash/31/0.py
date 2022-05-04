
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-1 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    return hashlib.sha1(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_file(filename):
    """
    Ach batlh ghIlghameS 'filename' neH sha-1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test.txt') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()

def ghop_D_hash_file_chunks(filename, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH sha-1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('test.txt') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            sha1.update(chunk)
    return sha1.hexdigest()

def ghop_D_hash_file_chunks_threaded(filename, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'filename' neH sha-1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks_threaded('test.txt') == '7b502c3a1f48c8609ae212cdfb639dee39673f5