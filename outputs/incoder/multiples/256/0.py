
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The sum of these multiples is 6.
    Return the sum of all the multiples of 2 or 5 below 197.
    """    
    sum = 0
    for i in range(1, 201):
        if i % 5 == 0 or i % 2 == 0:
            sum += i
    return sum

# Problem 4
def fibonacci(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
    832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986,
    102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073,
    4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571273,
    139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781905,
    4052739537881, 6557470319842, 10610209857723, 17167680177564, 267914296162, 4334944372639, 7014087334434,
    11349031703140, 18363119032930, 29712150730928, 48075269765056, 77787420491214, 125862690255057,
    203650110742788, 329512800990033, 533162911735456, 862675712730679, 139583862445978, 225851433717205,
    365435296162725, 591286729879936, 956722026041064, 154800875592137, 250473078190585, 405273953788189,
    655747031984272, 1061020985772337, 1716768017756479, 2679142961627251, 4334944372639519, 701408733443482,
    11349031703