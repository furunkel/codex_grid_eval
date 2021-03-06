
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest third value.
    """
    lst = sorted(lst)
    return lst[2]

# Test Cases
print(fibonacci([(3,1), (5,2), (8,3)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6), (25,7)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6), (25,7), (30,8)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6), (25,7), (30,8), (35,9)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6), (25,7), (30,8), (35,9), (40,10)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6), (25,7), (30,8), (35,9), (40,10), (45,11)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6), (25,7), (30,8), (35,9), (40,10), (45,11), (50,12)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6), (25,7), (30,8), (35,9), (40,10), (45,11), (50,12), (55,13)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6), (25,7), (30,8), (35,9), (40,10), (45,11), (50,12), (55,13), (60,14)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6), (25,7), (30,8), (35,9), (40,10), (45,11), (50,12), (55,13), (60,14), (65,15)]))
print(fibonacci([(3,1), (5,2), (8,3), (10,4), (15,5), (20,6), (25,7), (30,8), (35,9), (40,10), (45,11), (50,12), (55,13), (60,14), (65,15), (70,16)]))
print(