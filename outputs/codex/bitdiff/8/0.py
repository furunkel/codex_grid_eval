
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly four bit positions.
    """
    return bin(a ^ b).count('1') == 4


def main():
    """
    Solves the problem.
    """
    # Read the input.
    with open(INPUT_FILE) as input_file:
        lines = [line.strip() for line in input_file]

    # Find the two IDs that differ at exactly four bit positions.
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            if bit_diff(lines[i], lines[j]):
                print(lines[i])
                print(lines[j])
                break


if __name__ == '__main__':
    main()