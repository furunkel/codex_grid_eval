
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly five bit positions.
    """
    return bin(a ^ b).count('1') == 5


def main():
    """
    Solves the problem.
    """
    # Read the input.
    with open('input.txt') as input_file:
        lines = input_file.readlines()

    # Parse the input.
    ids = [line.strip() for line in lines]

    # Find the two IDs that differ at exactly five bit positions.
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            if bit_diff(ids[i], ids[j]):
                # Print the common letters.
                print(''.join(
                    [
                        chr(ids[i][k])
                        for k in range(len(ids[i]))
                        if ids[i][k] == ids[j][k]
                    ]
                ))

                # Stop searching.
                return


if __name__ == '__main__':
    main()