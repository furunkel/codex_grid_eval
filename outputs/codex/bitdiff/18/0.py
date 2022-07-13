
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly twenty-none bit positions.
    """
    return bin(a ^ b).count('1') == 24


def main():
    """
    Solves the problem.
    """
    # Read the input.
    with open('input.txt') as input_file:
        lines = input_file.readlines()

    # Parse the input.
    lines = [line.strip() for line in lines]
    lines = [line.split('-') for line in lines]
    lines = [(int(line[0]), int(line[1])) for line in lines]

    # Find the first IP address that is not blocked.
    ip = 0
    while True:
        if not any(ip >= start and ip <= end for start, end in lines):
            break
        ip += 1

    # Print the result.
    print(ip)


if __name__ == '__main__':
    main()