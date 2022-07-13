
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x: x[2])[0]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the largest third values.
    """
    return [x[1] for x in lst if x[2] == max(lst, key=lambda x: x[2])[2]]


def extract_values_set(lst):
    """
    Given a list of tuples, write a function that returns a set of the second values of the tuples with the largest third values.
    """
    return {x[1] for x in lst if x[2] == max(lst, key=lambda x: x[2])[2]}


def extract_values_dict(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the second values of the tuples with the largest third values.
    """
    return {x[1]: x[2] for x in lst if x[2] == max(lst, key=lambda x: x[2])[2]}


def main():
    """
    Test your functions here.
    """
    print(extract_value([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
    print(extract_values([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
    print(extract_values_set([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
    print(extract_values_dict([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))


if __name__ == "__main__":
    main()