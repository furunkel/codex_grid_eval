
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return (b,a,b-a)

def make_tuple_of_tuples(b):
    """
    Given a list, return a tuple where:
    The first element contains the sum of the first element of each tuple in the list.
    The second element contains the sum of the second element of each tuple in the list.
    The third element contains the sum of the third element of each tuple in the list.
    """
    return (b[0]+b[1]+b[2], b[0]+b[1]+b[2]-b[1], b[0]+b[1]+b[2]-b[1]-b[0])

def make_tuple_of_tuples_with_tuples(b):
    """
    Given a list, return a tuple where:
    The first element contains the sum of the first element of each tuple in the list.
    The second element contains the sum of the second element of each tuple in the list.
    The third element contains the sum of the third element of each tuple in the list.
    The fourth element contains the sum of the fourth element of each tuple in the list.
    """
    return (b[0]+b[1]+b[2]+b[3], b[0]+b[1]+b[2]+b[3]-b[1], b[0]+b[1]+b[2]+b[3]-b[1]-b[0], b[0]+b[1]+b[2]+b[3]-b[1]-b[0]-b[2])

def make_tuple_of_tuples_with_tuples_with_tuples(b):
    """
    Given a list, return a tuple where:
    The first element contains the sum of the first element of each tuple in the list.
    The second element contains the sum of the second element of each tuple in the list.
    The third element contains the sum of the third element of each tuple in the list.
    The fourth element contains the sum of the fourth element of each tuple in the list.
    The fifth element contains the sum of the fifth element of each tuple in the list.
    """
    return (b[0]+b[1]+b[2]+b[3]+b[4], b[0]+b[1]+b[2]+b[3]+b[4]-b[1], b[0]+b[1]+b[2]+b[3]+b[4]-b[1]-b[0], b[0]+b[1]+b[2]+b[3]+b[4]-b[1]-b[0]-b[2], b[0]+b[1]+b[2]+b[3]+b[4]-b[1]-b[0]-b[2]-b[3])

def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples(b):
    """
    Given a list, return a tuple where:
    The first element contains the sum of the first element of each tuple in the list.
    The second element contains the sum of the second element of each tuple in the list.
    The third element contains the sum of the third element of each tuple in the list.
    The fourth element contains the sum of the fourth element of each tuple in the list.
    The fifth element contains the sum