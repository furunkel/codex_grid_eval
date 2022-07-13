
def decr_list(l: list):
    """Return list with elements decremented by 1.
    >>> decr_list([1, 2, 3])
    [0, 1, 2]
    """
    return [x - 1 for x in l]


def get_neighbors(x: int, y: int, width: int, height: int):
    """Return list of neighbors of (x, y) in a grid of size width x height.
    >>> get_neighbors(0, 0, 3, 3)
    [(0, 1), (1, 0), (1, 1)]
    >>> get_neighbors(1, 1, 3, 3)
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    return [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)
            if 0 <= x + i < width and 0 <= y + j < height]


def get_neighbors_8(x: int, y: int, width: int, height: int):
    """Return list of neighbors of (x, y) in a grid of size width x height.
    >>> get_neighbors_8(0, 0, 3, 3)
    [(0, 1), (1, 0), (1, 1)]
    >>> get_neighbors_8(1, 1, 3, 3)
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    return [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)
            if 0 <= x + i < width and 0 <= y + j < height and (i, j) != (0, 0)]


def get_neighbors_4(x: int, y: int, width: int, height: int):
    """Return list of neighbors of (x, y) in a grid of size width x height.
    >>> get_neighbors_4(0, 0, 3, 3)
    [(0, 1), (1, 0)]
    >>> get_neighbors_4(1, 1, 3, 3)