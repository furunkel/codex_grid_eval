
def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA1 hash equivalent string.
    If the file does not exist, return None.

    >>> get_file_hash('test.txt') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if not os.path.isfile(filename):
        return None
    else:
        with open(filename, 'r') as f:
            return string_to_hash(f.read())


def get_file_hash_from_url(url):
    """
    Given a URL, return its SHA1 hash equivalent string.
    If the URL does not exist, return None.

    >>> get_file_hash_from_url('http://www.cs.cmu.edu/~spok/grimmtmp/073.txt') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    try:
        response = urllib2.urlopen(url)
        return string_to_hash(response.read())
    except urllib2.HTTPError:
        return None


def get_file_hash_from_url_cache(url):
    """
    Given a URL, return its SHA1 hash equivalent string.
    If the URL does not exist, return None.
    If the URL has been visited before, return the cached result.

    >>> get_file_hash_from_url_cache('http://www.cs.cmu.edu/~spok/grimmtmp/073.txt') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if url in url_cache:
        return url_cache[url]
    else:
        url_cache[url] = get_file_hash_from_url(url)
        return url_cache[url]


def get_file_