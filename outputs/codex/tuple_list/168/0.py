
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest third value.
    """
    return min(lst, key=lambda x: x[2])[2]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the smallest third values.
    """
    return [x[2] for x in lst if x[2] == extract_value(lst)]


def extract_values_set(lst):
    """
    Given a list of tuples, write a function that returns a set of the third values of the tuples with the smallest third values.
    """
    return set(extract_values(lst))


def extract_values_generator(lst):
    """
    Given a list of tuples, write a function that returns a generator of the third values of the tuples with the smallest third values.
    """
    return (x[2] for x in lst if x[2] == extract_value(lst))


def main():
    """
    Test your functions.
    """
    lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21)]
    print(extract_value(lst))
    print(extract_values(lst))
    print(extract_values_set(lst))
    print(list(extract_values_generator(lst)))


if __name__ == '__main__':
    main()