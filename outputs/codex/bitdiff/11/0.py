
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 5 bit positions.
    """
    return bin(a ^ b).count('1') == 5


def main():
    """
    Entry point.
    """
    with open('input.txt') as f:
        ids = [line.strip() for line in f]

    for i, id1 in enumerate(ids):
        for id2 in ids[i + 1:]:
            if bit_diff(id1, id2):
                print(''.join(c1 for c1, c2 in zip(id1, id2) if c1 == c2))
                return


if __name__ == '__main__':
    main()