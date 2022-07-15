
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return (a*b, a+b, a-b)


def make_tuple_of_tuples(tuple_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the sum of the second element of each tuple.
    The third element contains the product of the second element of each tuple.
    The fourth element contains the product of the first element of each tuple.
    The fifth element contains the difference of the second element of each tuple (first - second).
    """
    sum_of_first_elements = 0
    sum_of_second_elements = 0
    product_of_second_elements = 1
    product_of_first_elements = 1
    difference_of_second_elements = 1
    for tuple_of_tuples in tuple_of_tuples:
        sum_of_first_elements += tuple_of_tuples[0]
        sum_of_second_elements += tuple_of_tuples[1]
        product_of_second_elements = tuple_of_tuples[1] * product_of_second_elements
        product_of_first_elements = tuple_of_tuples[0] * product_of_first_elements
        difference_of_second_elements = tuple_of_tuples[1] - tuple_of_tuples[2]
    return (sum_of_first_elements, sum_of_second_elements, product_of_second_elements, product_of_first_elements, difference_of_second_elements)


def make_tuple_of_tuples_with_tuples(tuple_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the sum of the second element of each tuple.
    The third element contains the product of the second element of each tuple.
    The fourth element contains the product of the first element of each tuple.
    The fifth element contains the difference of the second element of each tuple (first - second).
    The sixth element contains the difference of the first element of each tuple (second - first).
    """
    sum_of_first_elements = 0
    sum_of_second_elements = 0
    product_of_second_elements = 1
    product_of_first_elements = 1
    difference_of_second_elements = 1
    difference_of_first_elements = 1
    for tuple_of_tuples in tuple_of_tuples:
        sum_of_first_elements += tuple_of_tuples[0]
        sum_of_second_elements += tuple_of_tuples[1]
        product_of_second_elements = tuple_of_tuples[1] * product_of_second_elements
        product_of_first_elements = tuple_of_tuples[0] * product_of_first_elements
        difference_of_second_elements = tuple_of_tuples[1] - tuple_of_tuples[2]
        difference_of_first_elements = tuple_of_tuples[2] - tuple_of_tuples[0]
    return (sum_of_first_elements, sum_of_second_elements, product_of_second_elements, product_of_first_elements, difference_of_second_elements, difference_of_first_elements)