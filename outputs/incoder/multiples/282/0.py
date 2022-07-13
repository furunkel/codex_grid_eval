
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5, 3 or 2, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 5, 3 or 2 below 124.
    """    
    sum = 0
    for i in range(125, 1, -1):
        if i % 5 == 0 or i % 3 == 0 or i % 2 == 0:
            sum += i
    return sum

# Problem 4
def fibonacci(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946,
    17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040,
    1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169,
    63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170,
    1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074,
    32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162,
    615749715484, 1088128359025, 1720507390095, 273747669162, 445733010821, 704874467162,
    1170305068438, 1814853488145, 3099436239513, 5265908055111, 8944395397471,
    14472334024229, 2169376924321, 3224379737671, 4935707055781, 7552879493757,
    12847770396179, 19586457477695, 3177737590273, 5142297580151, 8320439348237,
    13462696712229, 21783097747265, 35245781471279, 57028878078809, 92274665395575,
    14930352809479, 24157817263733, 39088169578675, 63245985871387, 102334154493382,
    165580142296625, 267914295943777, 4334944