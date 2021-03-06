
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return max(lst, key=lambda x:x[1])[0]

# Test Cases
print(min_max([(5,3), (2,3), (1,3), (4,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3)]))
print(min_max([(5,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,3), (4,3), (3,3), (2,3), (1,