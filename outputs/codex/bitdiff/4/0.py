
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly two bit positions.
    """
    return bin(a ^ b).count('1') == 2


def find_pair(numbers):
    """
    Finds the pair of numbers that differ at exactly two bit positions.
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if bit_diff(numbers[i], numbers[j]):
                return numbers[i], numbers[j]


def find_common_bits(a, b):
    """
    Returns the common bits of two numbers that differ at exactly two bit
    positions.
    """
    return a & ~(a ^ b)


def main():
    numbers = read_input()
    a, b = find_pair(numbers)
    print(find_common_bits(a, b))


if __name__ == '__main__':
    main()