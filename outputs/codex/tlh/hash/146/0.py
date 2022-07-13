
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3_512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    return hashlib.sha3_512(vIdaj.encode('utf-8')).hexdigest()

def ghop_D_hash_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3_512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    return ghop_D_hash(vIdaj)

def ghop_D_hash_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3_512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_ghItlh_ghItlh('Hallo welt') == '4bc49cca273fb299acf8f8991b6547b6232a2344f289ed60db3159ac500b01df5c24bc1575465e701a514608eecde9c9bac18619be39132b96ddf28d2bc2c25b'
    """
    return ghop_D_hash(vIdaj)

def ghop_D_hash_ghItlh_ghItlh_ghItlh(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha3_512 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.