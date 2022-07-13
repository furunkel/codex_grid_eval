
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest third value.
    """
#    print(lst)
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0][0]
    if len(lst) == 2:
        return lst[0][1] + lst[1][0]
    if len(lst) == 3:
        return lst[0][1] + lst[1][1] + lst[2][0]
    if len(lst) == 4:
        return lst[0][1] + lst[1][1] + lst[2][1] + lst[3][0]
    if len(lst) == 5:
        return lst[0][1] + lst[1][1] + lst[2][1] + lst[3][1] + lst[4][0]
    if len(lst) == 6:
        return lst[0][1] + lst[1][1] + lst[2][1] + lst[3][1] + lst[4][1] + lst[5][0]
    if len(lst) == 7:
        return lst[0][1] + lst[1][1] + lst[2][1] + lst[3][1] + lst[4][1] + lst[5][1] + lst[6][0]
    if len(lst) == 8:
        return lst[0][1] + lst[1][1] + lst[2][1] + lst[3][1] + lst[4][1] + lst[5][1] + lst[6][1] + lst[7][0]
    if len(lst) == 9:
        return lst[0][1] + lst[1][1] + lst[2][1] + lst[3][1] + lst[4][1] + lst[5][1] + lst[6][1] + lst[7][1] + lst[8][0]
    if len(lst) == 10:
        return lst[0][1] + lst[1][1] + lst[2][1] + lst[3][1] + lst[4][1] + lst[5