
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The third element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The second element contains the sum of the two numbers.
    """
    return (a-b,a*b,a+b)

def make_tuple_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple of tuples where:
    The first element of each tuple contains the sum of the first element of each tuple.
    The second element of each tuple contains the product of the first element of each tuple.
    The third element of each tuple contains the difference of the first element of each tuple.
    """
    return tuple(tuple(sum(tuple_list[0]),
                      tuple_list[0]*tuple_list[1],
                      tuple_list[0]-tuple_list[1])
                 for tuple_list in tuples)

def make_tuple_of_tuples_with_tuples(tuples):
    """
    Given a list of tuples, return a tuple of tuples where:
    The first element of each tuple contains the sum of the first element of each tuple.
    The second element of each tuple contains the product of the first element of each tuple.
    The third element of each tuple contains the difference of the first element of each tuple.
    The fourth element of each tuple contains the sum of the second element of each tuple.
    The fifth element of each tuple contains the product of the second element of each tuple.
    The sixth element of each tuple contains the difference of the second element of each tuple.
    """
    return tuple(tuple(sum(tuple_list[0]),
                      tuple_list[0]*tuple_list[1],
                      tuple_list[0]-tuple_list[1],
                      sum(tuple_list[1]),
                      tuple_list[1]*tuple_list[2],
                      tuple_list[1]-tuple_list[2])
                 for tuple_list in tuples)

def make_tuple_of_tuples_with_tuples_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple of tuples where:
    The first element of each tuple contains the sum of the first element of each tuple.
    The second element of each tuple contains the product of the first element of each tuple.
    The third element of each tuple contains the difference of the first element of each tuple.
    The fourth element of each tuple contains the sum of the second element of each tuple.
    The fifth element of each tuple contains the product of the second element of each tuple.
    The sixth element of each tuple contains the difference of the second element of each tuple.
    The seventh element of each tuple contains the sum of the third element of each tuple.
    The eighth element of each tuple contains the product of the third element of each tuple.
    The ninth element of each tuple contains the difference of the third element of each tuple.
    """
    return tuple(tuple(sum(tuple_list[0]),
                      tuple_list[0]*tuple_list[1],
                      tuple_list[0]-tuple_list[1],
                      sum(tuple_list[1]),
                      tuple_list[1]*tuple_list[2],
                      tuple_list[1]-tuple_list[2],
                      sum(tuple_list[2]),
                      tuple_list[2]*tuple_list[3],
                      tuple_list[2]-tuple_list[3],
                      sum(tuple_list[3]),
                      tuple_list[3]*tuple