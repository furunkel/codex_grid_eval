
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x: x[2])[2]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the largest third values.
    """
    return [x[2] for x in lst if x[2] == max(lst, key=lambda x: x[2])[2]]


def extract_values_set(lst):
    """
    Given a list of tuples, write a function that returns a set of the third values of the tuples with the largest third values.
    """
    return {x[2] for x in lst if x[2] == max(lst, key=lambda x: x[2])[2]}


def main():
    """
    Run sample extract_value functions.
    """
    a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    b = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 8, 9)]
    c = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
    print(extract_value(a))
    print(extract_value(b))
    print(extract_value(c))
    print(extract_values(a))
    print(extract_values(b))
    print(extract_values(c))
    print(extract_values_set(a))
    print(extract_values_set(b))
    print(extract_values_set(c))


if __name__ == "__main__":
    main()