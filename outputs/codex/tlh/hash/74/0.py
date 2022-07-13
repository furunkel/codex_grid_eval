
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    return hashlib.sha384(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    return ghop_D_hash(vIdaj)

def ghop_D_hash_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    return ghop_D_hash(vIdaj)

def ghop_D_hash_ghItlh_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh_ghItlh