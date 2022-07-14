def string_sequence(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(100)
    '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100'
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


def string_to_int(s: str) -> int:
    """ Convert a string to an integer.
    >>> string_to_int('0')
    0
    >>> string_to_int('1')
    1
    >>> string_to_int('2')
    2
    >>> string_to_int('3')
    3
    >>> string_to_int('4')
    4
    >>> string_to_int('5')
    5
    >>> string_to_int('6')
    6
    >>> string_to_int('7')
    7
    >>> string_to_int('8')
    8
    >>> string_to_int('9')
    9
    >>> string_to_int('10')
    10
    >>> string_to_int('11')
    11
    >>> string_to_int('12')
    12
    >>> string_to_int('13')
    13
    >>> string_to_int('14')
    14
    >>> string_to_int('15')
    15
    >>> string_to_int('16')
    16
    >>> string_to_int('17')
    17
    >>> string_to