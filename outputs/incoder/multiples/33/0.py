
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 5, we get 2, 4, 5, 6 and 8. The product of these multiples is 1920.
    Return the product of all the multiples of 2 or 5 below 197.
    """    
    
    multiples = []
    for i in range(2, int(math.sqrt(197)) + 1):
        if i % 2 == 0:
            if i % 5 == 0:
                multiples.append(i)
            else:
                multiples.append(i * 5)
        else:
            multiples.append(i * 2)
    return multiples[len(multiples) - 1]

def fibonacci():
    """
    Using math module, find the nth fibonacci number using recursion.
    """
    
    fibs = []
    fibs.append(0)
    fibs.append(1)
    
    def fibonacci_rec(num):
        if num == 0:
            return fibs[0]
        elif num == 1:
            return fibs[1]
        else:
            return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)
    
    return fibonacci_rec(int(input("Enter the nth fibonacci number: ")))

def fibonacci_iter():
    """
    Using math module, find the nth fibonacci number using iteration.
    """
    
    fibs = []
    fibs.append(0)
    fibs.append(1)
    
    def fibonacci_iter(num):
        a, b = 0, 1
        while num > 0:
            fibs.append(a)
            a, b = b, a + b
            num -= 1
        return fibs[len(fibs) - 1]
    
    return fibonacci_iter(int(input("Enter the nth fibonacci number: ")))

def fibonacci_memo():
    """
    Using math module, find the nth fibonacci number using memoization.
    """
    
    fibs = []
    fibs.append(0)
    fibs.append(1)
    
    def fibonacci_memo(num):
        if num in fibs:
            return fibs[num]
        else:
            if num == 0:
                fibs.append(0)
            elif num == 1:
                fibs.append(1)
            else:
                fibs.append(fibonacci_memo(num - 1) + fibonacci_memo(num - 2))
            return fibs[num]
    
    return fibonacci_memo(int(input("Enter the nth fibonacci number: ")))

def fibonacci_memo_iter():
    """
    Using math module, find the nth fibonacci number using memoization.
    """
    
    fibs = []
    fibs.append(0)
    fibs.append(1)
    
    def fibonacci_memo_iter(num):
        a, b = 0, 1
        while num > 0:
            fibs.append(a)
            a, b = b, a + b
            num -= 1
        return fibs[len(fibs) - 1]
    
