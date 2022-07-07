
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest last value.
    """
    return max(text, key=lambda x: x[1])[0]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with the largest last value.
    """
    return [x[0] for x in text if x[1] == max(text, key=lambda x: x[1])[1]]


def extract_values_set(text):
    """
    Given a list of tuples, write a function that returns a set of the first values of each tuple with the largest last value.
    """
    return {x[0] for x in text if x[1] == max(text, key=lambda x: x[1])[1]}


def extract_values_dict(text):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple with the largest last value.
    """
    return {x[0]: x[1] for x in text if x[1] == max(text, key=lambda x: x[1])[1]}


def main():
    """
    Main function.
    """
    text = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    print(extract_value(text))
    print(extract_values(text))
    print(extract_values_set(text))
    print(extract_values_dict(text))


if __name__ == '__main__':
    main()