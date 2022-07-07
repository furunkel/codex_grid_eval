
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[2]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the smallest third values.
    """
    return [x[2] for x in text if x[2] == extract_value(text)]


def extract_values_set(text):
    """
    Given a list of tuples, write a function that returns a set of the third values of the tuples with the smallest third values.
    """
    return set(extract_values(text))


def extract_values_dict(text):
    """
    Given a list of tuples, write a function that returns a dictionary of the third values of the tuples with the smallest third values.
    """
    return {x[2]: x for x in text if x[2] == extract_value(text)}


def main():
    """
    Given a list of tuples, write a function that returns a dictionary of the third values of the tuples with the smallest third values.
    """
    text = [('a', 'b', 1), ('a', 'b', 2), ('x', 'y', 3), ('x', 'y', 0)]
    print(extract_value(text))
    print(extract_values(text))
    print(extract_values_set(text))
    print(extract_values_dict(text))


if __name__ == '__main__':
    main()