
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest first value.
    """
    
    lst = sorted(lst)
    return lst[2][1]

#Test Cases
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd')]))
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd'), (6, 'e'), (4, 'f')]))
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd'), (6, 'e'), (4, 'f'), (7, 'g')]))
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd'), (6, 'e'), (4, 'f'), (7, 'g'), (8, 'h')]))
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd'), (6, 'e'), (4, 'f'), (7, 'g'), (8, 'h'), (9, 'i')]))
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd'), (6, 'e'), (4, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j')]))
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd'), (6, 'e'), (4, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j'), (11, 'k')]))
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd'), (6, 'e'), (4, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j'), (11, 'k'), (12, 'l')]))
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd'), (6, 'e'), (4, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j'), (11, 'k'), (12, 'l'), (13, 'm')]))
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd'), (6, 'e'), (4, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j'), (11, 'k'), (12, 'l'), (13, 'm'), (14, 'n')]))
print(extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd'), (6, 'e'), (4, 'f'), (7, 'g'), (8, 'h'), (