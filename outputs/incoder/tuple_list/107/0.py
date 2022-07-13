
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x:x[2])[1]

#______________________________________________________________________________
# Problem 5
def max_min_search(lst):
    """
    Given a list of tuples, write a function that returns the tuple with the smallest second value and the largest third value.
    """
    return min(lst, key=lambda x:x[2])[2], max(lst, key=lambda x:x[2])[2]

#______________________________________________________________________________
# Problem 6
def max_min_search2(lst):
    """
    Given a list of tuples, write a function that returns the tuple with the smallest second value and the largest third value.
    """
    smallest = lst[0]
    largest = lst[0]
    for x in lst:
        if x[2] < largest[2]:
            largest = smallest
            smallest = x
        elif x[2] > largest[2]:
            largest = x
    return smallest, largest

#______________________________________________________________________________
# Problem 7
def max_min_search3(lst):
    """
    Given a list of tuples, write a function that returns the tuple with the smallest second value and the largest third value.
    """
    smallest = lst[0]
    largest = lst[0]
    for x in lst:
        if x[2] < smallest[2]:
            smallest = x
        elif x[2] > largest[2]:
            largest = x
    return smallest, largest

#______________________________________________________________________________
# Problem 8
def max_min_search4(lst):
    """
    Given a list of tuples, write a function that returns the tuple with the smallest second value and the largest third value.
    """
    smallest = lst[0]
    largest = lst[0]
    for x in lst:
        if x[2] < smallest[2]:
            smallest = x
        elif x[2] > largest[2]:
            largest = x
    return smallest, largest

#______________________________________________________________________________
# Problem 9
def max_min_search5(lst):
    """
    Given a list of tuples, write a function that returns the tuple with the smallest second value and the largest third value.
    """
    smallest = lst[0]
    largest = lst[0]
    for x in lst:
        if x[2] < smallest[2]:
            smallest = x
        elif x[2] > largest[2]:
            largest = x
    return smallest, largest

#______________________________________________________________________________
# Problem 10
def max_min_search6(lst):
    """
    Given a list of tuples, write a function that returns the tuple with the smallest second value and the largest third value.
    """
    smallest = lst[0]
    largest = lst[0]
    for x in lst:
        if x[2] < smallest[2]:
            smalle