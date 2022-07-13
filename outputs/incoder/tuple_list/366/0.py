
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
    """
    return max(lst, key=lambda x:x[0])[1]

# Write a function that takes a list of tuples and returns the last value of the tuple with the largest first value.
# Test your function below.
def extract_value_test(lst):
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c')]) == 'c'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd')]) == 'd'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd'), (4, 'e')]) == 'e'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd'), (4, 'e'), (0, 'f')]) == 'f'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd'), (4, 'e'), (0, 'f'), (0, 'g')]) == 'g'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd'), (4, 'e'), (0, 'f'), (0, 'g'), (0, 'h')]) == 'h'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd'), (4, 'e'), (0, 'f'), (0, 'g'), (0, 'h'), (0, 'i')]) == 'i'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd'), (4, 'e'), (0, 'f'), (0, 'g'), (0, 'h'), (0, 'i'), (0, 'j')]) == 'j'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd'), (4, 'e'), (0, 'f'), (0, 'g'), (0, 'h'), (0, 'i'), (0, 'j'), (0, 'k')]) == 'k'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd'), (4, 'e'), (0, 'f'), (0, 'g'), (0, 'h'), (0, 'i'), (0, 'j'), (0, 'k'), (0, 'l')]) == 'l'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd'), (4, 'e'), (0, 'f'), (0, 'g'), (0, 'h'), (0, 'i'), (0, 'j'), (0, 'k'), (0, 'l'), (0, 'm')]) == 'm'
    assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd'), (4, 'e'), (0, 'f'), (0, 'g'), (0, 'h'), (0, 'i'), (0, 'j'), (0, 'k'), (0, '