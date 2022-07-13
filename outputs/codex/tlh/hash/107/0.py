
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    return hashlib.sha512(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-512 hash ghopDu' qIj.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_qIj('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    return hashlib.sha512(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_qIj_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-512 hash ghopDu' qIj.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_qIj_qIj('md5') == 'fa39a630d203fd86c87d4a1f5d1e88a4496206f3c10b8c40858c8e0fbaef0889f46b9b4924b072d63170826a921b6f560cf68e1700c132077cd3f64cf269b548'
    """
    return hashlib.sha512(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_qIj_qIj_qIj(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-512 hash ghopDu