
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly six bit positions.
    """
    return bin(a ^ b).count('1') == 6


def main():
    """
    Solves the problem.
    """
    # Read the input.
    with open(INPUT_FILE) as input_file:
        lines = input_file.read().splitlines()

    # Parse the input.
    numbers = [int(line) for line in lines]

    # Find the two numbers that differ at exactly six bit positions.
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if bit_diff(numbers[i], numbers[j]):
                print(numbers[i], numbers[j])
                return


if __name__ == '__main__':
    main()