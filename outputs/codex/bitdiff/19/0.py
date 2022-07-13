
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 29 bit positions.
    """
    return bin(a ^ b).count('1') == 29


def main():
    """
    Solves the problem.
    """
    # The number of possible values for the first two digits is
    # (10 choose 2) * (8 choose 2) * (6 choose 2) * (4 choose 2) * (2 choose 2)
    # = 10 * 28 * 15 * 6 * 1 = 25200
    #
    # The number of possible values for the last two digits is
    # (10 choose 2) * (8 choose 2) * (6 choose 2) * (4 choose 2) * (2 choose 2)
    # = 10 * 28 * 15 * 6 * 1 = 25200
    #
    # The number of possible values for the middle two digits is
    # (10 choose 2) * (8 choose 2) * (6 choose 2) * (4 choose 2) * (2 choose 2)
    # = 10 * 28 * 15 * 6 * 1 = 25200
    #
    # The number of possible values for the middle two digits is
    # (10 choose 2) * (8 choose 2) * (6 choose 2) * (4 choose 2) * (2 choose 2)
    # = 10 * 28 * 15 * 6 * 1 = 25200
    #
    # The number of possible values for the middle two digits is
    # (10 choose 2) * (8 choose 2) * (6 choose 2) * (4 choose 2) * (2 choose 2)
    # = 10 * 28 * 15 * 6 * 1 = 25200
    #
    # The number of possible values for the middle two digits is
    # (10 choose 2) * (8 choose 2) * (6 choose 2) * (4 choose 2) * (2 choose 2)
    # = 10 * 28 * 15 * 6 * 1 = 25200
    #
    # The number of possible values for the middle two digits is
    # (10 choose 2) * (8 choose 2) * (6 choose 2) * (4 choose 2) * (2 choose 2)
    # = 10 * 28 * 15 * 6 * 1 = 25200
    #
    # The number of possible values for the middle two digits is
    # (10 choose 2) * (