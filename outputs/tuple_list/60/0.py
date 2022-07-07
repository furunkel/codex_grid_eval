
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
    return min(text, key=lambda x: x[1])[0]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of values with the smallest last value.
    """
    return [x[0] for x in text if x[1] == min(text, key=lambda x: x[1])[1]]


def main():
    """
    Main function.
    """
    # Test cases
    print(extract_value([(1, 7), (4, 6), (3, 9)]))
    print(extract_value([(9, 7), (4, 6), (3, 9)]))
    print(extract_value([(9, 7), (4, 6), (9, 9)]))
    print(extract_value([(1, 1), (4, 1), (3, 1)]))
    print(extract_value([(1, 7), (4, 6), (3, 9), (9, 1)]))
    print(extract_value([(1, 7), (4, 6), (3, 9), (9, 1), (2, 4)]))
    print(extract_value([(1, 7), (4, 6), (3, 9), (9, 1), (2, 4), (9, 0)]))
    print(extract_value([(1, 7), (4, 6), (3, 9), (9, 1), (2, 4), (9, 0), (3, 8)]))
    print(extract_value([(1, 7), (4, 6), (3, 9), (9, 1), (2, 4), (9, 0), (3, 8), (8, 2)]))
    print(extract_value([(1, 7), (4, 6), (3, 9), (9, 1), (2, 4), (9, 0), (3, 8), (8, 2), (2, 3)]))
    print(extract_value([(1, 7), (4, 6), (3, 9), (9, 1), (2, 4), (9, 0), (3, 8),