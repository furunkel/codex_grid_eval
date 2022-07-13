
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der MD5-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def zeichenkette_zu_sha1(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA1-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_sha1('Hello world') == '2ef7bde608ce5404e97d5f042f95f89f1c232871'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def zeichenkette_zu_sha256(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA256-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_sha256('Hello world') == '7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def zeichenkette_zu_sha512(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA512-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurü