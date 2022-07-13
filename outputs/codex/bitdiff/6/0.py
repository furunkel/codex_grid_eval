
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly three bit positions.
    """
    return bin(a ^ b).count('1') == 3


def find_correct_box_ids(box_ids):
    """
    Finds the two box IDs that differ at exactly three bit positions.
    """
    for i in range(len(box_ids)):
        for j in range(i + 1, len(box_ids)):
            if bit_diff(box_ids[i], box_ids[j]):
                return box_ids[i], box_ids[j]


def find_common_letters(a, b):
    """
    Finds the common letters between two box IDs.
    """
    return ''.join(chr(x) for x in a if chr(x) in b)


def main():
    box_ids = [int(x) for x in read_input()]
    a, b = find_correct_box_ids(box_ids)
    print(find_common_letters(a, b))


if __name__ == '__main__':
    main()