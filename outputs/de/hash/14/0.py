
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der md-5-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('Hallo welt') == '05b7f4cbafdb32436fe8928f41ed8f64'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def zeichenkette_zu_sha1(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha1-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_sha1('Hallo welt') == 'f8c7e8f9b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def zeichenkette_zu_sha256(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha256-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_sha256('Hallo welt') == 'f8c7e8f9b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def zeichenkette_zu_sha512(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sh