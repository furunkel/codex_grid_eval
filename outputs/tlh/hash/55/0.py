
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    return hashlib.sha256(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_file(file_name):
    """
    Ach batlh ghIlghameS 'file_name' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'file_name' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test.txt') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    with open(file_name, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def ghop_D_hash_file_chunks(file_name, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'file_name' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'file_name' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_chunks('test.txt') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    h = hashlib.sha256()
    with open(file_name, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def ghop_D_hash_file_chunks_threaded(file_name, chunk_size=1024):
    """
    Ach batlh ghIlghameS 'file_name' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'file_name' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_