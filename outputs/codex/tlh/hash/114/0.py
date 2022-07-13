
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2B hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2b(vIdaj, digest_size=32)


def ghop_D_hash_hex(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2B hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2b(vIdaj, digest_size=32).hexdigest()


def ghop_D_hash_hex_short(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2B hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2b(vIdaj, digest_size=32).hexdigest()[:8]


def ghop_D_hash_hex_long(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2B hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2b(vIdaj, digest_size=32).hexdigest()[:16]


def ghop_D_hash_hex_long_long(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2B hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2b(vIdaj, digest_size=32).hexdigest()[:32]


def ghop_D_hash_hex_long_long_long(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2B hash ghopDu.
    qaSbe'chugh