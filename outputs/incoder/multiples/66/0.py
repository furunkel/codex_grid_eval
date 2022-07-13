
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8 and 9. The sum of these multiples is 37.
    Return the sum of all the multiples of 5, 3 or 2 below 600.
    """    
    sum = 0
    for i in range(600):
        if i % 5 == 0 and i % 3 == 0 or i % 2 == 0:
            sum += i
    return sum

# Problem 4
def fibonacci(n):
    """
    Fibonacci numbers are the numbers in the following manner:
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
    317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465,
    14930352, 24157817, 39088169, 63245986, 102334155, 165580141,
    267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073,
    4807526976, 7778742049, 12586269025, 20365011074, 32951280099,
    53316291173, 86267571272, 139583862445, 225851433717, 365435296162,
    615754557661, 991948530103, 160500643829, 298389622397, 469700099989,
    777894755979, 1259710651055, 2033709730481, 3239543929697, 532245786221,
    862675712725, 1396163294775, 2260574597881, 3654352961625, 6157770954737,
    9919501438577, 1605006438297, 2983896223977, 4697000999897, 7778947559797,
    12597106510559, 20337097304817, 32395439296977, 53224578622177, 86267571272537,
    139616329477537, 226057459788117, 365435296162537, 615777095473737, 991950143857777,
    160500643829777, 29838962239777, 469700099989767, 7778947559787, 1259710651055977,
    2033709730