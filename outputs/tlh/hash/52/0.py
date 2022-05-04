
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    return hashlib.new(vIdaj, ''.encode('utf-8')).hexdigest()

def ghop_D_hash_vaj_ghop_D_hash(vIdaj, ghop_D):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_vaj_ghop_D_hash('sha1', 'sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    return hashlib.new(vIdaj, ghop_D.encode('utf-8')).hexdigest()

def ghop_D_hash_vaj_ghop_D_hash_vaj_ghop_D_hash(vIdaj, ghop_D, ghop_D2):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-224 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_vaj_ghop_D_hash_vaj_ghop_D_hash('sha1', 'sha1', 'sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    return hashlib.new(vIdaj, (ghop_D + ghop_D2).encode('utf-8')).hexdigest()

def ghop_D_hash_vaj_ghop_D_hash_vaj_ghop_D_hash_vaj_ghop_D_hash(vIdaj, ghop_D, ghop_D2, ghop_D3):
    """
    Ach batlh ghIlghameS 'vIdaj' ne