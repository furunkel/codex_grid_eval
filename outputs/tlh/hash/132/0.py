
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2S hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2s(vIdaj).digest()


def ghop_D_hash_hex(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2S hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2s(vIdaj).hexdigest()


def ghop_D_hash_hex_short(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2S hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2s(vIdaj).hexdigest()[:8]


def ghop_D_hash_hex_long(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2S hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2s(vIdaj).hexdigest()[:32]


def ghop_D_hash_hex_long_long(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2S hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
    return blake2s(vIdaj).hexdigest()[:64]


def ghop_D_hash_hex_long_long_long(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH BLAKE2S hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.
    """
   