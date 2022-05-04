
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2s hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2s(vIdaj).hexdigest()

def ghop_D_hash_sha256(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return sha256(vIdaj).hexdigest()

def ghop_D_hash_sha512(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return sha512(vIdaj).hexdigest()

def ghop_D_hash_sha3_256(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3_256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return sha3_256(vIdaj).hexdigest()

def ghop_D_hash_sha3_512(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3_512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return sha3_512(vIdaj).hexdigest()

def ghop_D_hash_sha3_384(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3_384 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return sha3_384(vIdaj).hexdigest()

def