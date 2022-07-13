
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2b hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2b(vIdaj, digest_size=32).digest()


def ghop_D_hash_hex(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2b hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2b(vIdaj, digest_size=32).hexdigest()


def ghop_D_hash_hex_short(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2b hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2b(vIdaj, digest_size=32).hexdigest()[:8]


def ghop_D_hash_hex_long(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2b hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2b(vIdaj, digest_size=32).hexdigest()[:16]


def ghop_D_hash_hex_longer(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2b hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2b(vIdaj, digest_size=32).hexdigest()[:24]


def ghop_D_hash_hex_longest(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH blake2b hash ghopDu.
    qaSbe'chugh, vaj 'vId