
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 15 bit positions.
    """
    return bin(a ^ b).count('1') == 15


def main():
    """
    Entry point.
    """
    # Read the input.
    with open('input.txt') as f:
        lines = f.readlines()

    # Parse the input.
    ids = [line.strip() for line in lines]

    # Find the two IDs that differ at exactly 15 bit positions.
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            if bit_diff(ids[i], ids[j]):
                print(ids[i], ids[j])
                break


if __name__ == '__main__':
    main()