
def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return hashlib.sha256(text.encode()).hexdigest()


def hash_to_string(hash_value):
    """
    Given a hash value 'hash_value', return its string equivalent.
    If 'hash_value' is None, return an empty string.
    """
    if hash_value is None:
        return ""
    else:
        return hash_value


def hash_children(left_child, right_child):
    """
    Given the hash values of the left and right child nodes, return the hash value of the parent node.
    If either of the child nodes is None, return None.
    """
    if left_child is None or right_child is None:
        return None
    else:
        return hashlib.sha256((left_child + right_child).encode()).hexdigest()


def get_merkle_root(hashes):
    """
    Given a list of hash values, return the hash value of the root node of the Merkle tree.
    If the list is empty, return None.
    """
    if len(hashes) == 0:
        return None
    elif len(hashes) == 1:
        return hashes[0]
    else:
        while len(hashes) > 1:
            if len(hashes) % 2 == 1:
                hashes.append(hashes[-1])
            new_hashes = []
            for i in range(0, len(hashes), 2):
                new_hashes.append(hash_children(hashes[i], hashes[i+1]))
            hashes = new_hashes
        return hashes[0]


def get_merkle_path(merkle_root, leaf_hash):
    """
    Given the hash value of the root node of a Merkle tree and the hash value of a leaf node,
    return the Merkle path of the leaf node.
    If the leaf node is not in the tree, return None.
    """
    if leaf_hash not in merkle_root:
        return None
    else:
        path