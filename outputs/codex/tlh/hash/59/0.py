
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    return hashlib.sha256(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    return hashlib.sha256(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    return hashlib.sha256(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_ghItlh_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh_ghItlh('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4