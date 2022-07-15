
def make_tuple(fkrjf4ifji4ofj, fekjfwoeifjwu5gfd):
    """
    Given two integers fkrjf4ifji4ofj and fekjfwoeifjwu5gfd, return a tuple where:
    The third element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    third = fkrjf4ifji4ofj - fekjfwoeifjwu5gfd
    product = third * third
    sum = fkrjf4ifji4ofj + fekjfwoeifjwu5gfd
    return (third, product, sum)


# Problem 7
def make_tuple_of_tuples(fkrjf4ifji4ofj, fekjfwoeifjwu5gfd):
    """
    Given two integers fkrjf4ifji4ofj and fekjfwoeifjwu5gfd, return a tuple where:
    The first element contains a tuple containing the difference of the two numbers (first - second).
    The second element contains a tuple containing the product of the two numbers.
    The third element contains a tuple containing the sum of the two numbers.
    """
    third = fkrjf4ifji4ofj - fekjfwoeifjwu5gfd
    product = third * third
    sum = fkrjf4ifji4ofj + fekjfwoeifjwu5gfd
    return (make_tuple(third, product), make_tuple(sum, product))


# Problem 8
def make_tuple_of_tuples_2(fkrjf4ifji4ofj, fekjfwoeifjwu5gfd):
    """
    Given two integers fkrjf4ifji4ofj and fekjfwoeifjwu5gfd, return a tuple where:
    The first element contains a tuple containing the difference of the two numbers (first - second).
    The second element contains a tuple containing the product of the two numbers.
    The third element contains a tuple containing the sum of the two numbers.
    """
    third = fkrjf4ifji4ofj - fekjfwoeifjwu5gfd
    product = third * third
    sum = fkrjf4ifji4ofj + fekjfwoeifjwu5gfd
    return (make_tuple(third, product), make_tuple(sum, product), make_tuple(sum, third))


# Problem 9
def make_tuple_of_tuples_3(fkrjf4ifji4ofj, fekjfwoeifjwu5gfd):
    """
    Given two integers fkrjf4ifji4ofj and fekjfwoeifjwu5gfd, return a tuple where:
    The first element contains a tuple 