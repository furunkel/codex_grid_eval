
def ghop_D_hash(vIdaj):
    """
    Ach batlh ghIlghameS 'vIdaj' neH sha-256 hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.

    >>> ghop_D_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    return hashlib.sha256(vIdaj.encode('utf-8')).hexdigest()


def ghop_D_hash_file(filename):
    """
    Ach batlh ghIlghameS 'filename' neH sha-256 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file('test.txt') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def ghop_D_hash_file_md5(filename):
    """
    Ach batlh ghIlghameS 'filename' neH md5 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_md5('test.txt') == '3ebff31b62c0637c54d4ffa990d5c100'
    """
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def ghop_D_hash_file_sha1(filename):
    """
    Ach batlh ghIlghameS 'filename' neH sha-1 hash ghopDu.
    qaSbe'chugh, vaj 'filename' po'vaD qaS wanI'vam.

    >>> ghop_D_hash_file_sha1('test.txt') == 'ea359994b35f4b342ff49797542148cd'
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def ghop_D_hash_file_sha256(filename):
    """
    Ach batlh ghIlghameS